import torch.nn as nn
import scipy.signal as signal
import pandas as pd
import torch
import time
from pylsl import StreamInlet, resolve_stream
import torch.nn.functional as F


def notch_filter(data, fs=250, freq=50, quality_factor=30):
    b, a = signal.iirnotch(w0=freq, Q=quality_factor, fs=fs)
    return signal.filtfilt(b, a, data)


def notch_df_filter(df):
    fs = 250  # Sampling frequency of the EEG signals
    for col in df.columns:
        df[col] = notch_filter(df[col], fs=fs, freq=50)
    return df


def bandpass_filter(data, low, high, fs=250, order=5):
    nyquist = 0.5 * fs
    low = low / nyquist
    high = high / nyquist
    b, a = signal.butter(order, [low, high], btype='band')
    return signal.filtfilt(b, a, data)


brain_bands = ['EEG 1_theta',
               'EEG 2_theta',
               'EEG 3_theta',
               'EEG 4_theta',
               'EEG 5_theta',
               'EEG 6_theta',
               'EEG 7_theta',
               'EEG 8_theta',
               'EEG 1_alpha',
               'EEG 2_alpha',
               'EEG 3_alpha',
               'EEG 4_alpha',
               'EEG 5_alpha',
               'EEG 6_alpha',
               'EEG 7_alpha',
               'EEG 8_alpha',
               'EEG 1_beta',
               'EEG 2_beta',
               'EEG 3_beta',
               'EEG 4_beta',
               'EEG 5_beta',
               'EEG 6_beta',
               'EEG 7_beta',
               'EEG 8_beta',
               'EEG 1_gamma',
               'EEG 2_gamma',
               'EEG 3_gamma',
               'EEG 4_gamma',
               'EEG 5_gamma',
               'EEG 6_gamma',
               'EEG 7_gamma',
               'EEG 8_gamma']

mean_std = ['EEG 1_theta_mean',
            'EEG 1_theta_std',
            'EEG 2_theta_mean',
            'EEG 2_theta_std',
            'EEG 3_theta_mean',
            'EEG 3_theta_std',
            'EEG 4_theta_mean',
            'EEG 4_theta_std',
            'EEG 5_theta_mean',
            'EEG 5_theta_std',
            'EEG 6_theta_mean',
            'EEG 6_theta_std',
            'EEG 7_theta_mean',
            'EEG 7_theta_std',
            'EEG 8_theta_mean',
            'EEG 8_theta_std',
            'EEG 1_alpha_mean',
            'EEG 1_alpha_std',
            'EEG 2_alpha_mean',
            'EEG 2_alpha_std',
            'EEG 3_alpha_mean',
            'EEG 3_alpha_std',
            'EEG 4_alpha_mean',
            'EEG 4_alpha_std',
            'EEG 5_alpha_mean',
            'EEG 5_alpha_std',
            'EEG 6_alpha_mean',
            'EEG 6_alpha_std',
            'EEG 7_alpha_mean',
            'EEG 7_alpha_std',
            'EEG 8_alpha_mean',
            'EEG 8_alpha_std',
            'EEG 1_beta_mean',
            'EEG 1_beta_std',
            'EEG 2_beta_mean',
            'EEG 2_beta_std',
            'EEG 3_beta_mean',
            'EEG 3_beta_std',
            'EEG 4_beta_mean',
            'EEG 4_beta_std',
            'EEG 5_beta_mean',
            'EEG 5_beta_std',
            'EEG 6_beta_mean',
            'EEG 6_beta_std',
            'EEG 7_beta_mean',
            'EEG 7_beta_std',
            'EEG 8_beta_mean',
            'EEG 8_beta_std',
            'EEG 1_gamma_mean',
            'EEG 1_gamma_std',
            'EEG 2_gamma_mean',
            'EEG 2_gamma_std',
            'EEG 3_gamma_mean',
            'EEG 3_gamma_std',
            'EEG 4_gamma_mean',
            'EEG 4_gamma_std',
            'EEG 5_gamma_mean',
            'EEG 5_gamma_std',
            'EEG 6_gamma_mean',
            'EEG 6_gamma_std',
            'EEG 7_gamma_mean',
            'EEG 7_gamma_std',
            'EEG 8_gamma_mean',
            'EEG 8_gamma_std']

bands = {
    'theta': (4, 8),
    'alpha': (8, 13),
    'beta': (13, 30),
    'gamma': (30, 45)
}


def extract_brain_waves(df, fs):
    filtered_df = pd.DataFrame()
    for band_name, (low, high) in bands.items():
        for col in df.columns:
            filtered_df[f'{col}_{band_name}'] = bandpass_filter(df[col], low, high, fs=fs)
    for col in filtered_df.columns:
        filtered_df[f'{col}_mean'] = filtered_df[col].mean()
        filtered_df[f'{col}_std'] = filtered_df[col].std()

    filtered_df = filtered_df[mean_std]
    sample = filtered_df.iloc[[0]]

    return sample


class SimpleClassifier(nn.Module):
    def __init__(self, input_size, hidden_size=64):
        super(SimpleClassifier, self).__init__()
        self.fc1 = nn.Linear(input_size, hidden_size)
        self.fc2 = nn.Linear(hidden_size, 2)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = self.fc2(x)
        return x


class TransformerClassifier(nn.Module):
    def __init__(self, input_size, hidden_size=64, num_heads=2, num_layers=1):
        super(TransformerClassifier, self).__init__()

        self.fc1 = nn.Linear(input_size, hidden_size)

        encoder_layer = nn.TransformerEncoderLayer(d_model=hidden_size, nhead=num_heads)
        self.transformer_encoder = nn.TransformerEncoder(encoder_layer, num_layers=num_layers)

        self.fc2 = nn.Linear(hidden_size, 2)

    def forward(self, x):
        x = F.relu(self.fc1(x))
        x = x.unsqueeze(0)
        x = self.transformer_encoder(x)
        x = x.squeeze(0)
        x = self.fc2(x)
        return x


def load_model(input_size, model_path, model_type="simple"):
    if model_type == "simple":
        model = SimpleClassifier(input_size=input_size)
        model.load_state_dict(torch.load(model_path))
        model.eval()
        print(f"Model loaded from {model_path}")
    elif model_type == 'transformer':
        model = TransformerClassifier(input_size=input_size)
        model.load_state_dict(torch.load(model_path))
        model.eval()
        print(f"Model loaded from {model_path}")
    else:
        raise TypeError('model_type must be "simple" or "transformer"')
    return model


def predict(model, input_data):
    with torch.no_grad():
        input_data = torch.tensor(input_data, dtype=torch.float32)
        input_data = input_data.view(1, -1)  # Reshape to match the input dimensions
        output = model(input_data)
        _, predicted_class = torch.max(output, 1)
        return predicted_class.item()


# %%
def preporcess_data(df):
    df = df[200: 2000]
    df = notch_df_filter(df)
    df = extract_brain_waves(df, fs=250)
    return df.values


def record_data(inlet, duration=5):
    print("Start recording")
    eeg = ['EEG 1',
           'EEG 2',
           'EEG 3',
           'EEG 4',
           'EEG 5',
           'EEG 6',
           'EEG 7',
           'EEG 8']
    columns = ['Time', 'EEG 1',
               'EEG 2',
               'EEG 3',
               'EEG 4',
               'EEG 5',
               'EEG 6',
               'EEG 7',
               'EEG 8', 'AccX', 'AccY', 'AccZ',
               'Gyro1', 'Gyro2', 'Gyro3', 'Battery', 'Counter', 'Validation']
    data_dict = dict((k, []) for k in columns)
    start_time = time.time()

    while time.time() - start_time < duration:
        data, timestamp = inlet.pull_sample()
        all_data = [timestamp] + data

        for i, key in enumerate(columns):
            data_dict[key].append(all_data[i])

    data_df = pd.DataFrame.from_dict(data_dict)
    data_df = data_df[eeg]
    print("Done recording")
    return data_df


def init_model(model_path="model/model_transformer.pth", model_type="transformer"):
    loaded_model = load_model(input_size=64, model_path=model_path, model_type=model_type)

    return loaded_model

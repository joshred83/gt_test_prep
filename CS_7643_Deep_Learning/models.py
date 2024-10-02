
import torch.nn as nn

class VGGBlock(nn.Module):
    def __init__(self, in_channels, out_channels, num_convs):
        super(VGGBlock, self).__init__()
        layers = []
        for _ in range(num_convs):
            layers.append(nn.Conv2d(in_channels, out_channels, kernel_size=3, padding=1))
            layers.append(nn.ReLU(inplace=True))
            in_channels = out_channels  # Update in_channels for next layer
        
        # Add max pooling at the end of the block
        layers.append(nn.MaxPool2d(kernel_size=2, stride=2))
        
        # Combine layers into a sequential module
        self.block = nn.Sequential(*layers)
    
    def forward(self, x):
        return self.block(x)

# Example usage: A VGG block with 3 convolutional layers, input channels = 64, output channels = 128
vgg_block = VGGBlock(in_channels=64, out_channels=128, num_convs=3)





import torch
import torch.nn as nn

class InceptionBlock(nn.Module):
    def __init__(self, in_channels, out_1x1, red_3x3, out_3x3, red_5x5, out_5x5, pool_proj):
        super(InceptionBlock, self).__init__()
        
        # 1x1 convolution branch
        self.branch1 = nn.Conv2d(in_channels, out_1x1, kernel_size=1)
        
        # 1x1 -> 3x3 convolution branch
        self.branch2 = nn.Sequential(
            nn.Conv2d(in_channels, red_3x3, kernel_size=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(red_3x3, out_3x3, kernel_size=3, padding=1)
        )
        
        # 1x1 -> 5x5 convolution branch
        self.branch3 = nn.Sequential(
            nn.Conv2d(in_channels, red_5x5, kernel_size=1),
            nn.ReLU(inplace=True),
            nn.Conv2d(red_5x5, out_5x5, kernel_size=5, padding=2)
        )
        
        # 3x3 pooling -> 1x1 convolution branch
        self.branch4 = nn.Sequential(
            nn.MaxPool2d(kernel_size=3, stride=1, padding=1),
            nn.Conv2d(in_channels, pool_proj, kernel_size=1)
        )
    
    def forward(self, x):
        branch1 = self.branch1(x)
        branch2 = self.branch2(x)
        branch3 = self.branch3(x)
        branch4 = self.branch4(x)
        
        # Concatenate along the channel dimension
        outputs = torch.cat([branch1, branch2, branch3, branch4], dim=1)
        return outputs

# Example usage: An Inception block with specific output channel configurations
inception_block = InceptionBlock(in_channels=192, out_1x1=64, red_3x3=96, out_3x3=128, red_5x5=16, out_5x5=32, pool_proj=32)


class ResidualBlock(nn.Module):
    def __init__(self, in_channels, out_channels, stride=1, downsample=None):
        super(ResidualBlock, self).__init__()
        # 1x1, 3x3, 1x1 bottleneck architecture
        self.conv1 = nn.Conv2d(in_channels, out_channels, kernel_size=1, stride=stride)
        self.bn1 = nn.BatchNorm2d(out_channels)
        
        self.conv2 = nn.Conv2d(out_channels, out_channels, kernel_size=3, stride=1, padding=1)
        self.bn2 = nn.BatchNorm2d(out_channels)
        
        self.conv3 = nn.Conv2d(out_channels, out_channels * 4, kernel_size=1)
        self.bn3 = nn.BatchNorm2d(out_channels * 4)
        
        self.relu = nn.ReLU(inplace=True)
        self.downsample = downsample

    def forward(self, x):
        identity = x
        
        out = self.conv1(x)
        out = self.bn1(out)
        out = self.relu(out)

        out = self.conv2(out)
        out = self.bn2(out)
        out = self.relu(out)
        
        out = self.conv3(out)
        out = self.bn3(out)
        
        if self.downsample is not None:
            identity = self.downsample(x)
        
        # Adding the residual (skip connection)
        out += identity
        out = self.relu(out)
        
        return out

# Example usage: A residual block with downsampling (for cases where input and output dimensions don't match)
downsample = nn.Sequential(
    nn.Conv2d(64, 256, kernel_size=1, stride=2),
    nn.BatchNorm2d(256)
)
residual_block = ResidualBlock(in_channels=64, out_channels=64, stride=2, downsample=downsample)


import tensorflow as tf
from tensorflow.keras import layers

class InceptionBlock(tf.keras.layers.Layer):
    def __init__(self, out_1x1, red_3x3, out_3x3, red_5x5, out_5x5, pool_proj):
        super(InceptionBlock, self).__init__()
        
        # 1x1 convolution branch
        self.branch1 = layers.Conv2D(out_1x1, kernel_size=(1, 1), activation='relu')
        
        # 1x1 -> 3x3 convolution branch
        self.branch2 = tf.keras.Sequential([
            layers.Conv2D(red_3x3, kernel_size=(1, 1), activation='relu'),
            layers.Conv2D(out_3x3, kernel_size=(3, 3), padding='same', activation='relu')
        ])
        
        # 1x1 -> 5x5 convolution branch
        self.branch3 = tf.keras.Sequential([
            layers.Conv2D(red_5x5, kernel_size=(1, 1), activation='relu'),
            layers.Conv2D(out_5x5, kernel_size=(5, 5), padding='same', activation='relu')
        ])
        
        # 3x3 pooling -> 1x1 convolution branch
        self.branch4 = tf.keras.Sequential([
            layers.MaxPooling2D(pool_size=(3, 3), strides=(1, 1), padding='same'),
            layers.Conv2D(pool_proj, kernel_size=(1, 1), activation='relu')
        ])

    def call(self, inputs):
        branch1 = self.branch1(inputs)
        branch2 = self.branch2(inputs)
        branch3 = self.branch3(inputs)
        branch4 = self.branch4(inputs)
        
        # Concatenate along the channel axis
        return tf.keras.layers.Concatenate(axis=-1)([branch1, branch2, branch3, branch4])

# Example usage: An Inception block



class ResidualBlock(tf.keras.layers.Layer):
    def __init__(self, filters, stride=1, downsample=None):
        super(ResidualBlock, self).__init__()
        
        # 1x1, 3x3, 1x1 bottleneck architecture
        self.conv1 = layers.Conv2D(filters, kernel_size=(1, 1), strides=stride, activation=None)
        self.bn1 = layers.BatchNormalization()
        
        self.conv2 = layers.Conv2D(filters, kernel_size=(3, 3), padding='same', activation=None)
        self.bn2 = layers.BatchNormalization()
        
        self.conv3 = layers.Conv2D(filters * 4, kernel_size=(1, 1), activation=None)
        self.bn3 = layers.BatchNormalization()
        
        self.relu = layers.ReLU()
        self.downsample = downsample

    def call(self, inputs):
        identity = inputs
        
        out = self.conv1(inputs)
        out = self.bn1(out)
        out = self.relu(out)
        
        out = self.conv2(out)
        out = self.bn2(out)
        out = self.relu(out)
        
        out = self.conv3(out)
        out = self.bn3(out)
        
        if self.downsample is not None:
            identity = self.downsample(inputs)
        
        # Adding the residual (skip connection)
        out += identity
        out = self.relu(out)
        
        return out

# Example usage: A residual block with downsampling (for cases where input and output dimensions don't match)
downsample = tf.keras.Sequential([
    layers.Conv2D(256, kernel_size=(1, 1), strides=2, activation=None),
    layers.BatchNormalization()
])
residual_block = ResidualBlock(filters=64, stride=2, downsample=downsample)


class SelfAttentionBlock(nn.Module):
    def __init__(self, in_dim):
        super(SelfAttentionBlock, self).__init__()
        self.query_conv = nn.Conv2d(in_dim, in_dim // 8, kernel_size=1)
        self.key_conv = nn.Conv2d(in_dim, in_dim // 8, kernel_size=1)
        self.value_conv = nn.Conv2d(in_dim, in_dim, kernel_size=1)
        self.softmax = nn.Softmax(dim=-1)  # Softmax over the last dimension

    def forward(self, x):
        batch, channels, height, width = x.size()
        
        # Generate query, key, and value tensors
        query = self.query_conv(x).view(batch, -1, height * width).permute(0, 2, 1)  # (B, N, C)
        key = self.key_conv(x).view(batch, -1, height * width)  # (B, C, N)
        value = self.value_conv(x).view(batch, -1, height * width)  # (B, C, N)

        # Attention matrix
        attention = torch.bmm(query, key)  # (B, N, N)
        attention = self.softmax(attention)

        # Apply attention to the values
        out = torch.bmm(value, attention.permute(0, 2, 1))  # (B, C, N)
        out = out.view(batch, channels, height, width)
        
        return out + x  # Residual connection

# Example usage: Self-Attention block for input with 64 channels
self_attention_block = SelfAttentionBlock(in_dim=64)


# Coin Detector with OpenCV

Detect and count coins in images using Python and OpenCV.

## About

This project is a coin detection and counting application implemented in Python using OpenCV. It takes an image as input and uses image processing techniques to identify and count the coins present in the image.

## Example

[//]: # (Include a brief example or demonstration of your project.)

```python
from detect_coin import CoinDetector

# Load an image
detector = CoinDetector("images/coins.jpg")

# Detect and count coins
detector.detect_and_count_coins()

# Display the result
detector.display_result()

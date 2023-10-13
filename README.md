# Coin Detector with OpenCV

Detect and count coins in images using Python and OpenCV.

## About

This project is a coin detection and counting application implemented in Python using OpenCV. It takes an image as input and uses image processing techniques to identify and count the coins present in the image.

## Result

<img width="415" alt="image" src="https://github.com/dkim7405/CoinDetector/assets/122648295/ecb2c8e1-20ae-458c-b66d-3d5e27c880f8">

<img width="411" alt="image" src="https://github.com/dkim7405/CoinDetector/assets/122648295/4d0316f5-01be-4a37-930b-c913dd5fae28">

<img width="413" alt="image" src="https://github.com/dkim7405/CoinDetector/assets/122648295/93e5afcf-35e7-4922-8540-20c1f5fb85d4">

## Example

```python
from detect_coin import CoinDetector

# Load an image
detector = CoinDetector("images/coins.jpg")

# Detect and count coins
detector.detect_and_count_coins()

# Display the result
detector.display_result()
```

##Future Improvements

1. **Improved Accuracy:** Fine-tune the coin detection algorithm to increase accuracy, especially in challenging lighting conditions.

2. **Real-Time Detection:** Implement real-time coin detection using a webcam or live camera feed for dynamic coin counting.

3. **Currency Recognition:** Extend the project to recognize and classify different coin denominations based on their size and features.

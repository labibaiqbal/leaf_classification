# 🌱 SmartGrow: Leaf Classification 🍃

## 📖 Project Description  
SmartGrow is a deep learning system that automatically identifies indoor plant species from leaf images. Once identified, the system adjusts environmental factors (light, water, humidity) to the specific needs of each species, helping reduce premature plant deaths.  

---

## ✨ Features  
- Capture images using a **Raspberry Pi camera**  
- Preprocess images (resize, grayscale, thresholding, edge detection)  
- Classify plant species (e.g. basil, lemon) with a **Convolutional Neural Network (CNN)**  
- Provide predictions with confidence levels  
- Real-time environmental adaptation for healthier plants  
- Data augmentation (rotation, scaling, flipping, contrast adjustments, Gaussian noise) for robust training  

---

## 🛠 Tech Stack  

| Component            | Technology / Library      |
|----------------------|---------------------------|
| Programming Language | Python                    |
| Deep Learning        | TensorFlow                |
| Image Processing     | OpenCV, NumPy             |
| Hardware             | Raspberry Pi + Pi Camera  |
| Model                | Convolutional Neural Net (CNN) |

---

## 📊 Model Training & Results  
The graph below illustrates the accuracy and loss trends of the CNN model trained over 50 epochs. The loss curve begins at a high value (~2.0) and decreases sharply during the first few epochs, indicating that the model is effectively learning low-level features such as edges and simple patterns. After around 10 epochs, the curve flattens and steadily decreases, suggesting that overfitting is minimized and the model is generalizing well to unseen data. By the end of training, the loss stabilizes around **0.25**, while accuracy improves consistently from 25% and plateaus near **85%**. The smoothness of both curves, without major spikes or drops, confirms stable training and well-tuned hyperparameters (learning rate, batch size, optimizer). To further improve performance beyond 85%, the optimizer can be switched from Adam to **Ranger**, which combines Rectified Adam and Lookahead for faster and more stable convergence.  

<p align="center">
  <img width="665" height="432" alt="Training Accuracy" src="https://github.com/user-attachments/assets/e4a2f108-330d-4880-9bfb-8af5a02ab711" />
  <img width="665" height="432" alt="Training Loss" src="https://github.com/user-attachments/assets/fec6cece-ee56-4d58-bbae-202eb8bbcf24" />
</p>

---

## ⚙️ How to Use  

1. **Install dependencies**  
   ```bash
   pip install tensorflow opencv-python numpy

 """
 检测一个振荡的信号什么时候稳定，通过最大最小阈值的差进行判断
 """
  
  
import numpy as np

original_signal = np.array([1])
last_delta = np.array([0])
last_signal = original_signal   # 与初始信号值保持一样

EXTREME = [1., 0.]    # 初始的最大最小阈值，注意顺序与信号开始增大还是减小有关

eps = 1e-3    # 

while 1:
  """
  中间的处理代码
  """
  if abs(EXTREME[-1]-EXTREME[-2]) < eps:
    break
  if np.dot(last_delta, signal-last_signal) < 0:
    EXTREME.append(np.linalg.norm(signal-original_signal))
  last_delta = signal - last_signal
  last_signal = signal

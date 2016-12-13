import os
import struct
import numpy as np
from mnist_neural_net import NeuralNetMLP
import matplotlib.pyplot as plt
import pickle
import os
from load_data import load_image

    X_train, y_train = load_image('images/', kind='train')
    X_train.shape


    X_test, y_test = load_image('images', kind='t10k')
    X_test.shape

    # fig, ax = plt.subplots(nrows=2, ncols=5, sharex=True, sharey=True)
    # ax = ax.flatten()
    # for i in range(10):
    #     img = X_train[y_train == i][0].reshape(28, 28)
    #     ax[i].imshow(img, cmap='Greys', interpolation='nearest')
    # ax[0].set_xticks([])
    # ax[0].set_yticks([])
    # tight_layout()
    # show()

    # training

    nn = NeuralNetMLP(n_output=10,
                     n_features=X_train.shape[1],
                     n_hidden=50,
                     l2=0.1,
                     l1=0.0,
                     epochs=1000,
                     eta=0.001,
                     alpha=0.001,
                     decrease_const=0.00001,
                     minibatches=50,
                     shuffle=True,
                     random_state=1) 
    
    nn.fit(X_train, y_train, print_progress=True)

    plt.plot(range(len(nn.cost_)), nn.cost_, color='k')
    plt.ylim([0, 2000])
    plt.ylabel('Cost')
    plt.xlabel('Epochs * 50')
    plt.tight_layout()
    plt.show()

    nn.save("my_trained_model.json")

    dest = os.path.join('imageclassifier', 'pkl_objects')
    if not os.path.exists(dest):
        os.makedirs(dest)

    pickle.dump(nn, 
        open(os.path.join(dest, 'classifier.pkl'), 'wb'), protocol = 4)
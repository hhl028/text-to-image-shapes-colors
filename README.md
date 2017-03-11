# Text-to-image for Generic shapes / colors

Sent2Vec encoder and training code from the paper [Skip-Thought Vectors](http://arxiv.org/abs/1506.06726).
Skip thought implementation from https://github.com/ryankiros/skip-thoughts.

## Dependencies

To use the skip thought vectors and GAN, you will need to install these:

* Python 2.7
* Theano 0.7
* A recent version of [NumPy](http://www.numpy.org/) and [SciPy](http://www.scipy.org/)
* [scikit-learn](http://scikit-learn.org/stable/index.html)
* [NLTK 3](http://www.nltk.org/)
* [Keras](https://github.com/fchollet/keras) (for Semantic-Relatedness experiments only)
* [gensim](https://radimrehurek.com/gensim/) (for vocabulary expansion when training new models)
* Tensorflow

## Getting started
First create a Data directory:
    
    cd <project_directory>
    mkdir Data
    cd Data

Run the following commands in this <project_directory>/Data/ directory to pull the data files. They are LARGE.

    wget http://www.cs.toronto.edu/~rkiros/models/utable.npy
    wget http://www.cs.toronto.edu/~rkiros/models/btable.npy
    wget http://www.cs.toronto.edu/~rkiros/models/uni_skip.npz
    wget http://www.cs.toronto.edu/~rkiros/models/uni_skip.npz.pkl
    wget http://www.cs.toronto.edu/~rkiros/models/bi_skip.npz
    wget http://www.cs.toronto.edu/~rkiros/models/bi_skip.npz.pkl
    wget http://www.cs.toronto.edu/~rkiros/models/dictionary.txt


Open skipthoughts.py and set your local paths to the <project_directory>/Data/ folder. They are currently set to my path, just change them and run:
    
    python model.py

Note that this processing may take a while. A LONG while.

Credits:

Yukun Zhu, Ryan Kiros, Richard Zemel, Ruslan Salakhutdinov, Raquel Urtasun, Antonio Torralba, Sanja Fidler.
**"Aligning Books and Movies: Towards Story-like Visual Explanations by Watching Movies and Reading Books."** *arXiv preprint arXiv:1506.06724 (2015).*

    @article{zhu2015aligning,
        title={Aligning Books and Movies: Towards Story-like Visual Explanations by Watching Movies and Reading Books},
        author={Zhu, Yukun and Kiros, Ryan and Zemel, Richard and Salakhutdinov, Ruslan and Urtasun, Raquel and Torralba, Antonio and Fidler, Sanja},
        journal={arXiv preprint arXiv:1506.06724},
        year={2015}
    }

## License

[Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0)

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/4dcu-be/ClassifyingPenguins/HEAD)

# Classifying Palmer's Penguins

Here are some notebooks of various experiments to use Dirichlet based mixture models to classify a number of datasets like the Iris, Fish Market and Palmer Penguins datasets. You can play around with these notebooks on binder, though you might need to decrease the number of samples to avoid time-outs.

## Running the Notebook

You can open the notebooks on [Binder](https://mybinder.org/v2/gh/4dcu-be/ClassifyingPenguins/HEAD).

To get the code running locally the easiest option is using [Anaconda]

```bash
git clone https://github.com/4dcu-be/ClassifyingPenguins
cd ClassifyingPenguins
conda env create -f environment.yml
conda activate pymc3
jupyter notebook
```

In case you are running this on windows you might need to install libpython in the environment and you will need Visual Studio Code 2017 build tools (with the C tools, check the options).


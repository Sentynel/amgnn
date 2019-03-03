# Angry Metal Album Art Classification

Some code to run classification operations on the album art database extracted from Angry Metal
Guy.

## Requirements

You need Python with Jupyter notebooks and fastai installed. You should probably use a virtualenv
of some sort. Follow instructions from these projects to get set up.

## Bundled data

The database I extracted from AMG is included. No guarantees are made about the quality of the
data.

## Usage

Run `./make_indexes.py` first. You can edit this file to make adjustments to how categories are
determined.

Then you'll want to start your Jupyter notebook server and probably open `brvtality.ipynb` to
train the neural network. `most_brvtal.ipynb` extracts some interesting bits from the results.
`brvtality-folder.ipynb` lets you do the same thing as the latter script, but across an arbitrary
folder of images rather than the training data set.

`black-death.ipynb` works similarly but for telling black metal apart from death metal.

`good-bad.ipynb` attempts to do the same for telling good records apart from bad, but it doesn't
work.

## Apologies

No effort has been made to tidy up the code here, and I have no real idea what I'm doing with
the neural network libraries. Seems to work, though.

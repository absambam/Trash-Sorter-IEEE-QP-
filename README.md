# Trash Sorter
As Global Warming worsens, it's only becoming more clear that we need to switch over to more sustainable lifestyles, and that includes properly sorting our waste into trash, compost, and recycling instead of sending everything to the landfill. At UCSD, even though we have separate trash and recycling bins, because people often times do not separate their waste properly, the school ends up throwing everything into the landfill. To tackle this problem, we have designed a machine that looks at an item and, using image recognition, determines whether the item is trash, recyclable, or compostable, and then sorts it accordingly.

To use this code, you will need:
- Raspberry Pi + Pi Camera
- button switch
- breadboard
- servo
- stepper motor

Before we start with the programming, we'd highly recommend creating a virtual environment for the project.
You can do so with the command
`virtualenv --system-site-packages -p python3 ./venv` where 'venv' is the name you want to give to your project directory.
Then, to activate the virtual environment, use the command
`source ./venv/bin/activate`

Now that you've created and activated a virtual environment, let's start setting up our code.

First, enter your project directory and install TensorFlow using the command
`pip install --upgrade tensorflow`

You can either use our re-trained model, or you can follow [this tutorial on retraining TensorFlow] (https://codelabs.developers.google.com/codelabs/tensorflow-for-poets/) and make your own categories.

If you would rather not retrain the model yourself, then simply copy all of the code in this repository. 
Otherwise, only copy the files in scripts, and make a folder in your main project directory named 'tf_files', and then create another folder within that called 'images', where you'll make three folders representing the three categories we want to sort into, and add images to those folders for TensorFlow to use to retrain. Then, follow the instructions in the above-linked tutorial.

Now that we have TensorFlow set up, connect the stepper motor, servo, and button switch to your breadboard and Pi. Take note of which GPIO pins you connect everything to, because you may have to change the pin numbers in the source code depending on how you conenct everything.

Now go into the 'scripts' folder, and run the command
`python application.py`
And you should be all set!

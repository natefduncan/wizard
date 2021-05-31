# Wizard
Custom audio stream using text to speech and central server to help with memorizing quotes. Dedicated to Booker T. Washington, the Wizard of Tuskegee. 

# Installation
- With pip: `pip3 install memorize-wizard`.
- On server: `wizard server --host 0.0.0.0`.
- On client, initialize: `wizard init` and enter `<SERVER_IP>:8040`. 
- On client, add text files; `wizard add FILE`. 
- Visit `<SERVER_IP>:8040/play/<FILE>` without extension (.txt, etc.).

# Local Installation
- To create source distribution: `python setup.py sdist`
- To install locally: `pip3 install --editable .`
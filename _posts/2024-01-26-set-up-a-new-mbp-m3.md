---
layout: post
title: Set up a new Macbook Pro M3 Max for deep learning from scratch
date: 2024-01-26
categories: machinelearning
---

I just got the new Macbook Pro M3 Max as a personal deep learning machine, fully maxed out with the 40 core GPU, 128GiB of RAM, and (just) the 2TiB SSD.
It was a great purchase.
I set up this machine as a blank slate, instead of transfering from my 9 year old MBP whose [Python environment looks like this.](https://xkcd.com/1987/)

This is a log of installing the software needed to run Mixtral and Diffusers. I was able to have Diffusers and Mixtral running locally within 2 hours. This procedure is editted to remove my missteps -- I installed things to the wrong Python environment a few times. 

## Installing libraries and applications

Install the first applications:
1. iterm2
2. Chrome
3. Visual Studio Code
4. Google Drive. (This is where my Colab notebooks live.)

Rebind Caps Lock to Control.

Install XCode through the App store and XCode tools via the system prompt that appears when loading iTerm2 for the first time. Accept the license with `sudo xcodebuild -license`.

Next: I asked the internet and all my friends if I should go the conda route or Homebrew route. I went the homebrew route.

Install Homebrew from http://brew.sh.

Type `which pip3` a bunch of times. It's easy to mix up Python environments. I make sure to install everything to the Homebrew Python install.

Run `brew install python3`. 

At this point, the system path will still point to the old python3. Type `which python3`. I installed packages to the wrong python dir a few times. It's easiest to just close Iterm2 and reopen it at this point.

Type `which pip3` and `which python3` a bunch of times after starting a new terminal to make sure it's the right one.

Install python and brew packages:

```bash
which pip3  # Should say /opt/homebrew/bin/pip3
which pip  # Should say /opt/homebrew/bin/pip
pip3 install torch
python3 -c "import torch; print(torch.__path__)"  # Should print ['/opt/homebrew/lib/python3.11/site-packages/torch']
pip3 install numpy matplotlib
pip3 install jupyter
pip3 install transformers gradio scipy ftfy datasets tqdm accelerate
pip3 install diffusers
brew install cmake
brew install git-lfs
```

For LaTeX:

- Install the environment: `brew install --cask mactex`
- Install the ["LaTeX Workshop"](https://marketplace.visualstudio.com/items?itemName=James-Yu.latex-workshop) VS Code plugin to get previews.


## Running Diffusers

It took a few minutes to modify a preexisting colab notebook.

1. Change `'cuda'` to `'mps'` everywhere
2. `with autocast('mps')` does not work yet. (https://github.com/pytorch/pytorch/issues/88415)
3. `torch_dtype=torch.float16` does not work. 

The final snippet to generate the pipe is:
```python
pipe = StableDiffusionInpaintPipeline.from_pretrained(
    "runwayml/stable-diffusion-inpainting",
    revision="fp16",
    # torch_dtype=torch.float16,  # Generates black images if you leave it in.
    use_auth_token=True,
).to("mps")
```
and then just apply 1 \& 2 everywhere.


## Running LLMs

[Ollama](ollama.ai) is awesome. Just install it from https://github.com/ollama/ollama, and then `ollama run mixtral` just works!


## Storage usage

The Huggingface repository using git-lfs for Mistral weights is 55GiB and Mixtral is >100GiB, since there are multiple checkpoints in full precision. Ollama will only download one copy of the quantized weights, so it takes up less disk space.

Here is what model weight storage looks like now:
```bash
% ollama list
NAME                          	ID          	SIZE  	MODIFIED
codellama:34b                 	685be00e1532	19 GB 	2 weeks ago
deepseek-coder:1.3b-base-q4_1 	75c6c24f8b9a	856 MB	2 weeks ago
deepseek-coder:33b-base-q4_K_M	a205c1c80cf6	19 GB 	2 weeks ago
llama2:latest                 	78e26419b446	3.8 GB	2 weeks ago
mistral:latest                	61e88e884507	4.1 GB	2 weeks ago
mixtral:latest                	7708c059a8bb	26 GB 	2 weeks ago

% du -sh .cache/huggingface/hub/*
afq@malachi ~ % du -sh .cache/huggingface/hub/*
2.6G	.cache/huggingface/hub/models--CompVis--stable-diffusion-v1-4
139M	.cache/huggingface/hub/models--facebook--mms-tts-eng
2.6G	.cache/huggingface/hub/models--runwayml--stable-diffusion-inpainting
2.6G	.cache/huggingface/hub/models--timbrooks--instruct-pix2pix
4.0K	.cache/huggingface/hub/version.txt
4.0K	.cache/huggingface/hub/version_diffusers_cache.txt
```

So, the 2TiB SSD option that I chose is large enough.
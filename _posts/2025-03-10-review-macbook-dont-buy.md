---
layout: post
title: 1 Year Review of MacBook Pro M3 Max -- Don't buy for Deep Learning.
date: 2025-03-10
categories: machinelearning
---

## TL;DR: Don't buy Apple Silicon for deep learning projects.

**What works:**
- llama.cpp on Metal (and the whole stack: ollama, etc.)
- Tinygrad on Metal
- Jax and PyTorch on CPU

**What doesn't work:**
- PyTorch on Metal
- Jax on Metal
- Tensorflow on Metal

## Review
Last year I purchased a fully specced-out MacBook Pro M3 Max with 128GiB of RAM, at a total cost of about US$5700 including tax and warranty. I purchased it specifically for the 128GiB of RAM attached to the GPU with the intention of using it for ML projects, such as fine tuning LLMs.

After 1 year of usage, I can't recommend getting any Apple Silicon products if your goal is to do any model **training**.

The problem is not the GPUs themselves. Llama.cpp and Tinygrad work fine which each have their own independent support for Metal. These two packages are the saving grace of the Apple Silicon.

Apple provided Metal drivers for Jax and Pytorch --- but these are far from usable. GPU support for ML is actually **in an insidious state:** Jax and Torch will *run* but there are subtle bugs. There are some assert errors and warnings on incompatibilities (for example, Jax-metal would raise an error after trying to allocate a matrix over 64KiB in size) but most of the time **the bugs are silent!**

This cost me a few weeks of painful debugging on a side project:  I was writing a bot to play Codenames and trying to RL it. My experience owning the MacBook was as follows:
1. Stable Diffusion worked with some dtypes but returns black images (no warning or error) on other dtypes. I managed to get reasonable looking outputs.
2. Ollama works out of the box with GPU acceleration. I made a training set using self play of codenames with Ollama.
3. I loaded the dataset of rewards into TRL, which used PyTorch under the hood.
4. The model training would NaN!



I worked on debugging my loss function and tried different RL methods, checked for bugs in my dataset. After a few weeks, I realized that the problem was the Torch drivers! I couldn't replicate the self-play within Torch (I was using ollama for base model rollouts.) I eventually realized that not even GPT2 would run in Torch on GPU.

> Aside: This is a pretty funny task to give to an LLM: they implicitly know the game, follow the formatting instructions, and give reasonable CoTs. But when actually playing, 50% of the time the clue is "I am on the blue team so I will give the clue "BLUE 3" so my teammates pick the words marked as belonging to the blue team". 🙄 It seemed like a fun project to try RL.

As of today, I continue to run into issues when I try Jax and Torch on Metal, both recently crashing on experiments with small 100-parameter NNs. I use Tinygrad for all ML projects now.
> Review for Tinygrad: It's great!

## The not so bad:

**Local LLMs with llama.cpp.** I use Ollamac these days to run Llama3.3 as a local chat bot in addition to the big hosted chat bots.

**CPU RAM is still useful.** For running interprettability experiments, a 70B parameter model's parameters, hidden state, and kv cache can fit into RAM in a single Jupyter notebook. Torch CPU inference is trustworthy and fast enough.

There's so much RAM that I keep that notebook open, run other smaller experiments, using LLMs with ollama, watching videos, AND never closing a Chrome tab. (Chrome is using 8GiB right now.)

**I haven't needed to use a Cloud VM.** Modest projects fit on the MacBook. While the cost of this laptop was more than I would normally spend on a modest cloud GPU, an A100 with 80GiB is still expensive, but...

**Physical ownership decreases task-switch overhead.** Being able to keep my notebooks active for weeks on end removes the joy-dampening barrier of cost-sensitive managing of VMs, and ultimately increases productivity.



## What I would buy instead

I would do the following now:

- Buy the cheapest MacBook Air.
- Buy a [tinybox](https://tinygrad.org/) (I am still considering the tinybox.)

## Lessons learned:


### Don't trust your hardware.

I learned yet another layer of distrusting your hardware. For every machine, every library, every processing unit, and every update, I run reference models with a reference output from CPU inference.

One test I used is running GPT2 and compare logits and a generation output with greedy decoding to a reference generation.

 ```python
import transformers
gpt_tokenizer = transformers.AutoTokenizer.from_pretrained("gpt2")
gpt_model =  transformers.AutoModelForCausalLM.from_pretrained("gpt2").to('mps')
toks = gpt_tokenizer("The rain in Spain", return_tensors='pt').to('mps')
result = gpt_model.generate(
    **toks, generation_config=transformers.GenerationConfig(max_new_tokens=16, do_sample=False))
generated = gpt_tokenizer.batch_decode(result)[0]
assert gpt_model.device.type == 'mps'
assert generated == 'The rain in Spain has been so bad that the city of Barcelona has been forced to close its doors'
 ```

This test used to fail back in March 2024, where it would decode to `!!!!...`. It has since started passing for all smaller sized models.

But this is part of the difficulty with the system. Although those bugs have been fixed, there are still bugs. As mentioned, both Flax and Jax can crash on simple neural networks.

Just this weekend I ran into another subtle problem running a PDE learning PyTorch library. The library can learn a PDE on CPU, but on MPS, the model just slowly converges to a flatline over training.

### Driver and community lock-in is real.
NVIDIA really has a monopoly on accelerators. I am looking forward to more hardware options. Unless you are interested in accelerator debugging, it's not worth an individual's time to deal with hardware compatibility issues: just pay the NVIDIA premium. 

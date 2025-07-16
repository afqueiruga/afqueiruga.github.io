---
layout: post
title: AI driven science will advance by not replicating humans
date: 2025-07-16
categories: workflow
published: True
---
# AI driven Science

> Thoughts from ICLR about the fusion of AI scientists and world models. Human publishing is a limited system for science. Instead of training AI scientist agents to work like humans, I propose focusing on scaling world models, and training AI engineers to do that.

At ICLR, two completely new approaches to applying ML for scientific discovery have broken out: LLM-driven scientist agents, and world models. This makes for three camps applying ML to science:

1. Traditional ML for science: training “simple” problem-specific models, like protein models or PDE-solving models, using a lot of inductive bias on the data modality and network architecture.  
2. AIs as scientists: training LLMs to be an agent replicating the human process of ideation, data analysis, experimentation, and emitting LaTeX.  
3. World Models: pure video-driven large scale models that learn action inputs and physical laws from next-frame prediction on natural video and video game data.

Getting agents to fully automate science is a new optimistic goal for AI development. A couple that stood out to me are:

1. AgentReview -- simulating the peer review, rebuttal, and AC process. [https://agentreview.github.io/](https://agentreview.github.io/)   
2. PaperBench -- AI as a paper replicator [https://arxiv.org/pdf/2504.01848](https://arxiv.org/pdf/2504.01848)   
3. Sakana AI scientist -- AI as a hypothesis generator and experiment running agent which managed to get accepted. [https://sakana.ai/ai-scientist-first-publication/](https://sakana.ai/ai-scientist-first-publication/)   
4. Proposed by AgentReview, AI^2 -- as a closed loop system of AIs writing papers for AIs to read, AIs reviewing AI-written papers, and then synthesizing blog posts for humans to read.

These are AIs that are trying to replicate how humans do science. We're dressing up the shoggoth in a lab coat and giving it human tools:  
![An AI generated cartoon of a shoggoth wearing a lab coat holding a beaker.]({{ BASE_PATH }}/assets/world-models-over-scientists_files/shoggoth_scientist.png) 

Gi What is the actual goal of science? What processes are we trying to replicate and which are we trying to replace? In this approach, the modality of the AI is reading papers and submitting papers for peer review. However...

## Human publishing is a *terrible* way to do science

By imitating the human way of doing science we run against two barriers: firstly, the human social process introduces errors and bias, and secondly, human language adds an artificial layer of abstraction that obscures underlying patterns.

1. Human scientific publishing processes are fundamentally flawed:   
   1. What is the error rate of peer review? The [Sakana AI result](https://sakana.ai/ai-scientist-first-publication/) may also be interpreted that the false positive rate of peer review is 1/3.  
   2. There are incentive misalignments in academia. Is the training data of human publishing actually demonstrating truth-seeking? Would replicating human behavior bake the same biases into the AI scientists?  
   3. Here, AI reviewers and replicators may help improve the quality of human scientific output. But can we do better by breaking the human societal construct?   
   4. The paradigm of distilling scientific information into text and equations loses some information about the real world. The intermediate step of reporting tables of measurements and approximate equations limits the connections we can make.  
2. Is there a better way to transfer knowledge than human language? Can we design a system where we can backpropagate gradients through all scientific observations?  
3. Is there a barrier to human understanding? Can world knowledge actually be distilled into human language? There is no reason to believe that nature has "ground truth" rules that are human legible. Replicating language-based thought may hit a wall. Going after *inhuman learning* may be required to advance science indefinitely.

## AI Scientists are useful in the near term

We can actually integrate these AI scientists additively in several ways.

**Help the humans early:** AgentReview can be a peer review simulator to strengthen papers before submission. If I could invoke it early enough and simulate peer review a few times, I might find shortcomings in my papers and run new experiments during my drafting process.

**AIs can do replication work** that humans are **actively discouraged to do in academia**. Fortunately, the AIs don't suffer reputational damage. This is where the approach of Paperbench is promising. The AIs can do this very important but unfairly snubbed work. If the work goes 100x faster, it might be worth it for a human to publish an even larger replication study for less time.

**Integrate this all with peer review**: I think it is feasible to integrate these processes into a conference scale peer review process. The main constraints are:

1. *Time:* Peer review timeline is about a month. In that time, a conference such as ICLR could kick off a giant batch run of 10k AI replicators. By the time the human reviewers have read the paper, the AI generated report can be ready, and the human reviewers can judge how well the AI system was able to replicate the results. This may not work for all papers, but the reviewers and area chairs can decide.  
2. *Inference costs:* conference fees are already $\approx \$1k$. Add another +$100 or +$200 to the industry registration fees to fund the LLM inferences. We can afford it.  
3. *Experiment costs:* many ML and computer science papers can be run entirely in the cloud, but the costs do add up. I keep my papers under $100 of training costs, but that is $1M for the 10k papers! For papers with very expensive experiments, authors could be required to fund credits to the cloud cluster. The exceptions to the rule should be spelled out in the paper with sufficient data provided. In that case, we can still run the AI replicator and train it to reply with, "I'm pretty sure this experiment would be too costly to replicate, but this is how I analyzed the model checkpoints the authors submitted to verify that they are legitimate."

## So what is science?

I personally follow instrumentalist philosophy: Science is the task of creating tools that help us predict the future state of the world ([https://en.wikipedia.org/wiki/Instrumentalism](https://en.wikipedia.org/wiki/Instrumentalism)). In the extreme case of instrumentalism, the body of scientific literature is just a black box model that helps us predict the future. 

AI-as-a-scientist is replicating the way that humans discover inductive biases in data measurement. Those biases are limited measurement techniques (i.e. getting a single temperature measurement) and then seeking simple explainable equations.

Following the Bitter Lesson, I think we should be trying to use our compute powers to *remove* inductive biases. From the instrumentalist point of view, we should be seeking to remove all inductive biases and instead maximizing how much next-state data we ingest in our models and maxing out on compute-parameters. 

I think this implies the world modeling paradigm. We've seen multiple interactive world models that are trained on pure video. ICLR had many very impressive results on games (Genie [https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/](https://deepmind.google/discover/blog/genie-2-a-large-scale-foundation-world-model/), Gamengen, GameNGen with Doom [https://gamengen.github.io/](https://gamengen.github.io/)), but world models are used for real world tasks too: comma.ai has been using full end-to-end trained world models for self driving: [https://blog.comma.ai/mlsim](https://blog.comma.ai/mlsim) [https://arxiv.org/pdf/2504.19077](https://arxiv.org/pdf/2504.19077)). I am bullish that this can clearly be pushed to the limits to actually learn physics. I don't even think state-action inputs are required: video generators such as Veo 2 [https://deepmind.google/technologies/veo/veo-2/](https://deepmind.google/technologies/veo/veo-2/) also are learning physics and agent minds.  
![An AI generated cartoon of a giant shoggoth in space eating the earth with a tentacle holding a scientific report.]({{ BASE_PATH }}/assets/world-models-over-scientists_files/shoggoth_getting_fed.png)  
What I think we should focus on instead is interpretability of world models. We should be pushing data collection and pretraining of world models to the extreme and encompass as many modes as possible -- natural video of egocentric views and robotics, microscopy, satellite imagery, new input modalities for chemical reactions, etc -- and throw them all into the world model training recipe. That alone can give us a useful tool in a unified model that can predict anything -- from the instrumentalist point of view, a black box is a useful scientific artifact. If we care about the "why", we humans, perhaps with AI co-scientists, can then extract the inner circuits of the world model.

## How do AI Scientists fit into a world-model central view?

The LLM driven agents can still be useful to automate writing the code and preparing data for the world model pretraining and analysis. Fusing the two cartoon metaphors, the AI Scientists are working as ML engineers instead, feeding the massive world model:  
![An AI generated cartoon of a giant shoggoth eating a planet with small shoggoth scientists feeding it.]({{ BASE_PATH }}/assets/world-models-over-scientists_files/shoggoth_getting_fed.png)  
The AI Scientists don't make the discoveries themselves. The world model is at the center of extracting information from the world. The LLM scientist agents are in service of the world model and to distill information from it for humans.

## Validation of world models

Whether or not world models can fuel actual scientific discoveries is still open. I personally like to poke holes in ML for science. I'm actually still skeptical that current next frame prediction techniques learn physical representations good enough for say, robotics control. Here are some ideas I have on how to verify world models:

1. The coefficient of gravity must be learned somewhere in a video generator. Where is that 9.81? Can you identify a linear probe or an SAE feature for gravity? Can you intervene and change gravity in a video generator?  
2. Can you deconstruct a world model of an Atari game using circuits and extract a code implementation?  
3. Can you train a pure video model on a multi-agent scenario and extract separate circuits for each agent? Are there multiple distinct agent "minds" embedded into the world model? 

## Conclusions

1. It is feasible to integrate "AI scientists" into conference workflows early on.  
2. World models can leapfrog the human way of doing science, because the world model artifact will have more useful physics and be immediately applicable.  
3. Instead of AI agents that copy human publishing, we can get more scientific discoveries by making AI agents that engineer world models instead.

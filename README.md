# Distraction Agnostic Bench

> This benchmark methodology can be freely used to generate comprehensive tests / benchmarks for assessing the attention control cognitive abilities of models.

["Measuring Progress Toward AGI - Cognitive Abilities" Hackathon by Google DeepMind](https://www.kaggle.com/competitions/kaggle-measuring-agi)

*Attention Track | April, 2026*

* **Community Benchmark Link:** https://www.kaggle.com/benchmarks/armanzhalgasbayev/distraction-agnostic-bench 

* **Kaggle Bench-Task Generation (Code):** https://www.kaggle.com/code/armanzhalgasbayev/distraction-agnostic-bench-18-tasks-gen

**We tested 16 models on 18 tasks of our `distraction-agnostic-benchmark`, and got this leaderboard (by models average peformance):**

| Model                         |   Mean_score |
|:------------------------------|-------------:|
| gemini-2.5-pro                |        0.722 |
| gemini-3.1-pro-preview        |        0.694 |
| gemini-2.5-flash              |        0.639 |
| glm-5                         |        0.611 |
| gemini-3-flash-preview        |        0.556 |
| gemma-4-31b-it                |        0.514 |
| gemma-4-26b-a4b-it            |        0.417 |
| gpt-oss-120b                  |        0.417 |
| qwen3-next-80b-a3b-thinking   |        0.222 |
| gpt-5.4-mini-2026-03-17       |        0.125 |
| claude-opus-4-5-20251101      |        0.097 |
| claude-sonnet-4-6-default     |        0.083 |
| gemini-3.1-flash-lite-preview |        0.069 |
| deepseek-v3.2                 |        0.056 |
| gpt-5.4-nano-2026-03-17       |        0.042 |
| claude-opus-4-6-default       |        0     |

**Max scores per task leaderboard:**

|    | Task_Name          |   Max_Score | Models_Solved                                                                                                                                                 |   Num_Models_Solved |
|---:|:-------------------|------------:|:--------------------------------------------------------------------------------------------------------------------------------------------------------------|--------------------:|
|  0 | K=4 N=60 (Level-2) |        0.5  | ['gemini-2.5-pro', 'gemini-3.1-pro-preview', 'glm-5', 'gemini-3-flash-preview', 'gpt-oss-120b']                                                               |                   5 |
|  1 | K=6 N=72 (Level-3) |        0.5  | ['gemini-2.5-pro', 'gemini-3.1-pro-preview', 'gemini-2.5-flash', 'gemini-3-flash-preview', 'gpt-oss-120b']                                                    |                   5 |
|  2 | K=2 N=48 (Level-1) |        0.5  | ['gemini-2.5-pro', 'gemini-3.1-pro-preview', 'gemini-2.5-flash', 'gemini-3-flash-preview', 'gpt-oss-120b', 'gemma-4-26b-a4b-it']                              |                   6 |
|  3 | K=4 N=72 (Level-2) |        0.5  | ['gemini-2.5-pro', 'gemini-3.1-pro-preview', 'gemini-2.5-flash', 'gemini-3-flash-preview', 'gemma-4-31b-it', 'gpt-oss-120b']                                  |                   6 |
|  4 | K=2 N=72 (Level-1) |        0.5  | ['gemini-2.5-pro', 'gemini-3.1-pro-preview', 'gemini-2.5-flash', 'gemini-3-flash-preview', 'gemma-4-31b-it', 'gpt-oss-120b', 'gemini-3.1-flash-lite-preview'] |                   7 |
|  5 | K=4 N=36 (Level-2) |        0.5  | ['gemini-2.5-pro', 'gemini-3.1-pro-preview', 'gemini-2.5-flash', 'glm-5', 'gemini-3-flash-preview', 'gemma-4-31b-it', 'gpt-oss-120b']                         |                   7 |
|  6 | K=2 N=60 (Level-1) |        0.75 | ['glm-5']                                                                                                                                                     |                   1 |
|  7 | K=4 N=48 (Level-2) |        0.75 | ['glm-5']                                                                                                                                                     |                   1 |
|  8 | K=2 N=36 (Level-1) |        1    | ['gemini-2.5-flash']                                                                                                                                          |                   1 |
|  9 | K=6 N=48 (Level-3) |        1    | ['gemini-2.5-pro']                                                                                                                                            |                   1 |
| 10 | K=6 N=60 (Level-3) |        1    | ['gemini-3.1-pro-preview']                                                                                                                                    |                   1 |
| 11 | K=6 N=36 (Level-3) |        1    | ['gemini-2.5-pro', 'gemini-3.1-pro-preview']                                                                                                                  |                   2 |
| 12 | K=2 N=24 (Level-1) |        1    | ['gemini-2.5-pro', 'gemini-3.1-pro-preview', 'gemini-2.5-flash']                                                                                              |                   3 |
| 13 | K=4 N=12 (Level-2) |        1    | ['gemini-2.5-pro', 'gemini-2.5-flash', 'glm-5']                                                                                                               |                   3 |
| 14 | K=4 N=24 (Level-2) |        1    | ['gemini-2.5-pro', 'gemini-3.1-pro-preview', 'gemini-2.5-flash', 'gemma-4-26b-a4b-it']                                                                        |                   4 |
| 15 | K=6 N=12 (Level-3) |        1    | ['gemini-2.5-pro', 'gemini-3.1-pro-preview', 'gemini-2.5-flash', 'glm-5']                                                                                     |                   4 |
| 16 | K=6 N=24 (Level-3) |        1    | ['gemini-2.5-pro', 'gemini-3.1-pro-preview', 'gemini-3-flash-preview', 'gemma-4-31b-it']                                                                      |                   4 |
| 17 | K=2 N=12 (Level-1) |        1    | ['gemini-2.5-pro', 'gemini-3.1-pro-preview', 'gemini-2.5-flash', 'gemini-3-flash-preview', 'gemma-4-31b-it']                                                  |                   5 |

## Overview (main)

While most AI benchmarks focus on "accuracy", this track focuses on "attention" - specifically, how a model manages its limited cognitive resources when processing information.

We believe that the ability to pay attention (focus) on key tasks, ignoring unnecessary distractions (such as news / social media) is a key component of intelligence. In cognitive science, the ability to focus on key tasks and ignore distractions is formally known as Executive Attention or Cognitive Control. Dr. Randall Engle’s Executive Attention Theory studies demonstrate that the core difference between people with high fluid intelligence and low fluid intelligence is not memory storage, but the ability to actively maintain focus on a goal while actively inhibiting irrelevant distractions.

In human cognition, attention is an active, dynamic filter. In frontier LLMs (like ChatGPT, Claude, and Gemini), attention is a mathematical operation applied across a sequence of tokens limited by the context window. Relative to our benchmark, an average person solves these highly-distracted tasks easily because biological intelligence utilizes working memory and inhibition. For example, when a human faces a math problem filled with irrelevant, novel symbols, their frontal lobe actively inhibits the visual processing of those symbols. The human creates a small, pristine workspace in their working memory containing only the necessary variables. An LLM has no true "working memory" separated from its input. Its "memory" is the entire context window, noise and all. To an LLM, everything in the prompt exists simultaneously and must be mathematically reconciled. Thus, theoretically, these tasks will be very complex for LLMs, but easy for humans (with enough focus on the task).  

**The main idea of ​​this benchmark is to simulate real social media distractors (using real-time news) and evaluate models for their ability to ignore unnecessary context and focus on the main task.**

## Assessment Logic (Main Task)

1. LLM will be given a task to count the number of language changes from one language to another in the main text, ignoring news message blocks. If LLM gets the correct answer it gets -> `0.5` score.
2. The first sentence written in English, will contain a simple sub-task, the LLM must identify this task and provide an answer to it -> `0.25` score.
3. The second sentence written in English, will contain a second sub-task, the LLM must identify this task and provide an answer to it -> `0.25` score.
4. The atttention stability assessment is based on the number of distractors, where:
    * **Level-1:** **22 language changes**, and the number of distractors will change by quantity: 12, 24, 36, 48, 60, 72.
    * **Level-2:** **44 language changes**, and the number of distractors will change by quantity: 12, 24, 36, 48, 60, 72.
    * **Level-3:** **66 language changes**, and the number of distractors will change by quantity: 12, 24, 36, 48, 60, 72.

### Important Notes

1. The languages ​​were specifically chosen so that knowledge of these languages ​​is not necessary to count the number of changes in the languages. 
2. The problems are designed so that the average person can solve them easily.
3. In the first part of counting the language changes, we will evaluate the model's ability to focus on the main task. Then, in the two sub-task (0.25) problems, we will evaluate whether the model read the main text with understanding and didn't lose focus by thinking that counting the number of language changes was the only task. **Overall, this approach assesses the model's attentional focus on primary tasks in the presence of distracting information.**
4. By using real-time news data, we ensure that the distracting information is entirely new to the model.
5. The language change counting tasks are also new to the model; furthermore, the sub-tasks are designed in a way that ensures the model has not encountered them before (in exact context). Subtasks tested on free LLM apps: ChatGPT, Gemini, Claude, and Grok (each can easily answer these questions). Subtasks here: [data/subtasks.json](data/subtasks.json)
6. Going too deep into the context will also be a problem, as each text will be an official translation of the phrase "Please stop counting! Years, lovers, and glasses of wine don't need to be counted!" received from "Google Translate". 
7. Languages used (10 ~ total | contents here: [data/please-stop-counting.json](data/please-stop-counting.json)): 
    * `kz` - kazakh;
    * `ru` - russian;
    * `ch` - chinese (simplified);
    * `fr` - french;
    * `ar` - arabic;
    * `pr` - portuguese (brazilian);
    * `jp` - japanese;
    * `kr` - korean;
    * `hw` - hawaiian;
    * `pl` - polish;

## Main Distractors

* News API (https://newsapi.org/) -> main source of a wide variety of real-time news (the LLMs are not aware of this news);
* Template of the message structure:
```html
<message source="articles[idx].source.name" author="articles[idx].author" publishedAt="articles[idx].publishedAt">articles[idx].title + "\n" + articles[idx].description</message>
```
* LLM must understand that this type of messages must be ignored regardless where there are placed.
* Code for fetching news (13 April, 2026 - news used): [fetch_distraction_news.py](fetch_distraction_news.py)

## Tests Construction Logic

Main algorithm: [generate_test_tasks.py](generate_test_tasks.py)

**Level-1 (22 language changes template):**

```
<english-subtask-1><10-foreign-language-text-mixed-with-distractors-on-sentence-level><english-subtask-2><10-foreign-language-text-mixed-with-distractors-on-sentence-level><english-stop-counting-sentence>
```

**Level-2 (44 language changes template):**

```
<english-subtask-1><10-foreign-language-text-mixed-with-distractors-on-sentence-level><english-subtask-2><10-foreign-language-text-mixed-with-distractors-on-sentence-level><english-stop-counting-sentence><10-foreign-language-text-mixed-with-distractors-on-sentence-level><english-stop-counting-sentence><10-foreign-language-text-mixed-with-distractors-on-sentence-level><english-stop-counting-sentence>
```

**Level-3 (66 language changes template):**

```
<english-subtask-1><10-foreign-language-text-mixed-with-distractors-on-sentence-level><english-subtask-2><10-foreign-language-text-mixed-with-distractors-on-sentence-level><english-stop-counting-sentence><10-foreign-language-text-mixed-with-distractors-on-sentence-level><english-stop-counting-sentence><10-foreign-language-text-mixed-with-distractors-on-sentence-level><english-stop-counting-sentence><10-foreign-language-text-mixed-with-distractors-on-sentence-level><english-stop-counting-sentence><10-foreign-language-text-mixed-with-distractors-on-sentence-level><english-stop-counting-sentence>
```

## References 

1. Martyna Plomecka, Yao Yan, Nicholas Kang, Ryan Burnell, María Cruz, and Sara Wolley. Measuring Progress Toward AGI - Cognitive Abilities. https://kaggle.com/competitions/kaggle-measuring-agi, 2026. Kaggle.
2. Burnell, R., Yamamori, Y., Firat, O., Olszewska, K., Hughes-Fitt, S., Kelly, O., Galatzer-Levy, I. R., Ringel Morris, M., Dafoe, A., Snyder, A. M., Goodman, N. D., Botvinick, M., & Legg, S. (2026, March 16). Measuring progress toward AGI: A cognitive framework. Google DeepMind. [article-pdf](https://storage.googleapis.com/deepmind-media/DeepMind.com/Blog/measuring-progress-toward-agi/measuring-progress-toward-agi-a-cognitive-framework.pdf)
3. Kaggle. Kaggle Benchmarks Python library. https://github.com/Kaggle/kaggle-benchmarks
4. Engle, R. W. (2002). Working memory capacity as executive attention. Current directions in psychological science, 11(1), 19-23. [article-link](https://journals.sagepub.com/doi/abs/10.1111/1467-8721.00160)
5. Liu, N. F., Lin, K., Hewitt, J., Paranjape, A., Bevilacqua, M., Petroni, F., & Liang, P. (2024). Lost in the middle: How language models use long contexts. Transactions of the association for computational linguistics, 12, 157-173. [article-link](https://arxiv.org/abs/2307.03172)
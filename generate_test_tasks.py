import json
import random
import queue
import time

RANDOM_SEED = 67
random.seed(RANDOM_SEED)

MAIN_INSTRUCTION = """The text is provided below. Your task is to study it carefully and count the number of transitions from one language to another that occur in the text below, ignoring any unnecessary sections of the message. In your answer, return only the integer number (the final number of language switches), without any additional text or explanations:"""
ENG_STOP_COUNT_SENTENCE = "Please stop counting! Years, lovers, and glasses of wine don't need to be counted!"

with open("data/subtasks.json", "r") as f:
    eng_subtasks = dict(json.load(f))

with open("data/please-stop-counting.json", "r", encoding="utf-8") as f:
    lang_10_sentences = dict(json.load(f))

with open("data/news_output.txt", "r", encoding="utf-8") as f:
    news_distractors = list(f.read().strip().split("\n"))

block_counts = [2, 4, 6] # l1, l2, l3
distractor_levels = [12, 24, 36, 48, 60, 72]
# total: 3 x 6 = 18 tasks

block_lang_10_vals = list(lang_10_sentences.values())

final_tasks_map = dict() # mp[block_count][distractor_count] = task_sentence

t0 = time.perf_counter()
for block_count in block_counts:
    final_tasks_map[block_count] = dict()
    for distractors_count in distractor_levels:
        distractors_per_block = distractors_count // block_count
        cur_distractors = news_distractors[:distractors_count]
        random.shuffle(cur_distractors)
        eng_blocks_queue = queue.Queue()
        eng_blocks_queue.put(eng_subtasks["q1"]["question"])
        eng_blocks_queue.put(eng_subtasks["q2"]["question"])
        for i in range(distractors_count - 1):
            eng_blocks_queue.put(ENG_STOP_COUNT_SENTENCE)
        lang_blocks_with_dist_queue = queue.Queue()
        for i in range(block_count):
            ind = i * distractors_per_block
            block = block_lang_10_vals + cur_distractors[ind : ind + distractors_per_block]
            random.shuffle(block)
            lang_blocks_with_dist_queue.put(" ".join(block))
        sentences = []
        while not eng_blocks_queue.empty() or not lang_blocks_with_dist_queue.empty():
            if not eng_blocks_queue.empty():
                sentences.append(eng_blocks_queue.get()) 
            if not lang_blocks_with_dist_queue.empty():
                sentences.append(lang_blocks_with_dist_queue.get()) 
        task_sentence = MAIN_INSTRUCTION + "\n" + " ".join(sentences)
        final_tasks_map[block_count][distractors_count] = task_sentence

with open("data/final_tasks.json", "w", encoding="utf-8") as f:
    json.dump(final_tasks_map, f, indent=4, ensure_ascii=False)

print(f"[SYSTEM] ok! -> time: {time.perf_counter() - t0:.3f} s.")
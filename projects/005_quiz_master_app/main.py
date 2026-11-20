# -*- coding: utf-8 -*-
"""
5. Quiz Master App
Timed JSON-driven quiz with scoring, review and leaderboard storage.
"""

import json, random, time
from pathlib import Path

def run_quiz():
    questions = json.load(open("questions.json", "r", encoding="utf-8"))
    random.shuffle(questions)
    score = 0
    wrong = []
    start = time.time()
    for i, q in enumerate(questions, 1):
        print(f"\n{i}/{len(questions)} {q['question']}")
        for j, opt in enumerate(q["options"], 1):
            print(f"  {j}. {opt}")
        try:
            ans = int(input("Answer: ").strip())
        except Exception:
            ans = 0
        if ans == q["answer"]:
            print("  -> Correct!")
            score += 1
        else:
            print(f"  -> Incorrect! Correct answer was: {q['options'][q['answer'] - 1]}")
            wrong.append(q)
    elapsed = time.time() - start
    name = input("\nYour name [Player]: ").strip() or "Player"
    board = []
    if Path("leaderboard.json").exists():
        try:
            board = json.load(open("leaderboard.json", "r", encoding="utf-8"))
        except Exception:
            board = []
    board.append({"name": name, "score": score, "time": round(elapsed, 1)})
    board = sorted(board, key=lambda x: (-x["score"], x["time"]))[:10]
    json.dump(board, open("leaderboard.json", "w", encoding="utf-8"), indent=2)
    print(f"\nScore: {score}/{len(questions)} | Time: {elapsed:.1f}s")
    print("\nTop players:")
    for x in board:
        print(f"  {x['name']:<15} Score: {x['score']}  Time: {x['time']}s")

if __name__ == "__main__":
    run_quiz()

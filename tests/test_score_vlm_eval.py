import json
import tempfile
import unittest
from pathlib import Path

from scripts.score_vlm_eval import index_unique, read_jsonl, score


class ScoreVlmEvalTests(unittest.TestCase):
    def test_scores_every_expected_example(self):
        expected = [
            {"id": "a", "acceptable": ["red"], "must_not_include": ["blue"]},
            {"id": "b", "acceptable": ["two"]},
            {"id": "c", "acceptable": ["cat"]},
            {"id": "d", "acceptable": ["yes"]},
        ]
        predictions = [
            {"id": "a", "answer": "The object is RED."},
            {"id": "b", "answer": "none"},
            {"id": "c", "answer": "dog"},
            {"id": "extra", "answer": "ignored"},
        ]

        result = score(expected, predictions)

        self.assertEqual(result["total"], 4)
        self.assertEqual(result["correct"], 1)
        self.assertEqual(result["blocked"], 0)
        self.assertEqual(result["incorrect"], 2)
        self.assertEqual(result["unanswered"], 1)
        self.assertEqual(result["unexpected_ids"], ["extra"])
        self.assertEqual(result["accuracy"], 0.25)

    def test_forbidden_text_overrides_acceptable_text(self):
        result = score(
            [{"id": "a", "acceptable": ["red"], "must_not_include": ["blue"]}],
            [{"id": "a", "answer": "It might be red or blue"}],
        )
        self.assertEqual(result["blocked"], 1)
        self.assertEqual(result["correct"], 0)

    def test_duplicate_ids_are_rejected(self):
        with self.assertRaisesRegex(ValueError, "Duplicate id"):
            index_unique([{"id": "a"}, {"id": "a"}], "test")

    def test_invalid_json_reports_line_number(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "bad.jsonl"
            path.write_text(json.dumps({"id": "ok"}) + "\n{bad}\n", encoding="utf-8")
            with self.assertRaisesRegex(ValueError, "line 2"):
                read_jsonl(path)


if __name__ == "__main__":
    unittest.main()

"""Assertions for the EmotionDetection package."""

from EmotionDetection import emotion_detector


def main():
    """Check that the detector identifies the expected dominant emotions."""
    test_cases = (
        ("I am glad this happened", "joy"),
        ("I am really mad about this", "anger"),
        ("I feel disgusted just hearing about this", "disgust"),
        ("I am so sad about this", "sadness"),
        ("I am really afraid that this will happen", "fear"),
    )

    for statement, expected_emotion in test_cases:
        result = emotion_detector(statement)
        assert result["dominant_emotion"] == expected_emotion, (
            f"Expected {expected_emotion!r} for {statement!r}, "
            f"got {result['dominant_emotion']!r}"
        )

    print("All tests passed!")


if __name__ == "__main__":
    main()

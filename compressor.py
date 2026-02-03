import subprocess
import sys

def compress_context(history):
    if not history.strip():
        return "No history provided."

    try:
        # Try ScaleDown Python import
        from scaledown import ScaleDownCompressor

        compressor = ScaleDownCompressor(rate="auto")

        result = compressor.compress(
            context=history,
            prompt="Extract audience behavior concisely."
        )

        return result.compressed_prompt

    except Exception:
        # Fallback compression
        lines = history.split("\n")
        return "\n".join(lines[:8])

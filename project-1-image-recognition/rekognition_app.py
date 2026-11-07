#!/usr/bin/env python3
"""Detect objects and other labels in an image with Amazon Rekognition.

Examples:
    python rekognition_app.py --image ./photo.jpg
    python rekognition_app.py --bucket my-image-bucket --key photos/photo.jpg
    python rekognition_app.py --bucket my-image-bucket --key photos/photo.jpg --output results.json

AWS credentials and the default region are read from the standard boto3
configuration (for example, ``aws configure`` or environment variables).
"""

import argparse
import json
import sys
from pathlib import Path
from typing import Any, Dict

import boto3
from botocore.exceptions import BotoCoreError, ClientError


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Detect labels in an image using Amazon Rekognition."
    )
    source = parser.add_mutually_exclusive_group(required=True)
    source.add_argument(
        "--image",
        help="Path to a local image file (JPEG or PNG).",
    )
    source.add_argument(
        "--bucket",
        help="S3 bucket containing the image; use together with --key.",
    )
    parser.add_argument(
        "--key",
        help="S3 object key for the image (required when --bucket is used).",
    )
    parser.add_argument(
        "--max-labels",
        type=int,
        default=10,
        help="Maximum number of labels to return (default: 10).",
    )
    parser.add_argument(
        "--min-confidence",
        type=float,
        default=70.0,
        help="Minimum confidence percentage, from 0 to 100 (default: 70).",
    )
    parser.add_argument(
        "--output",
        help="Optional path to save the labels as JSON. Prints to the terminal otherwise.",
    )
    args = parser.parse_args()

    if args.bucket and not args.key:
        parser.error("--key is required when using --bucket")
    if args.image and args.key:
        parser.error("--key can only be used with --bucket")
    if not 1 <= args.max_labels <= 1000:
        parser.error("--max-labels must be between 1 and 1000")
    if not 0 <= args.min_confidence <= 100:
        parser.error("--min-confidence must be between 0 and 100")
    return args


def detect_labels(args: argparse.Namespace) -> list[Dict[str, Any]]:
    """Call Rekognition and return its label list."""
    rekognition = boto3.client("rekognition")
    request: Dict[str, Any] = {
        "MaxLabels": args.max_labels,
        "MinConfidence": args.min_confidence,
    }

    if args.image:
        image_path = Path(args.image)
        if not image_path.is_file():
            raise FileNotFoundError(f"Image file not found: {image_path}")
        request["Image"] = {"Bytes": image_path.read_bytes()}
    else:
        request["Image"] = {
            "S3Object": {"Bucket": args.bucket, "Name": args.key}
        }

    response = rekognition.detect_labels(**request)
    return response.get("Labels", [])


def main() -> int:
    args = parse_args()
    try:
        labels = detect_labels(args)
        result = json.dumps(labels, indent=4)

        if args.output:
            Path(args.output).write_text(result + "\n", encoding="utf-8")
            print(f"Detected {len(labels)} labels. Results saved to {args.output}")
        else:
            print(result)
        return 0
    except (BotoCoreError, ClientError, FileNotFoundError, OSError) as exc:
        print(f"Error: {exc}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())




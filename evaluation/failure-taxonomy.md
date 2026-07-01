# Failure Taxonomy for Multimodal Models

Use this taxonomy when testing VLMs manually or building an eval harness.

## Perception failures

- Misses an object
- Invents an object
- Gets color wrong
- Gets count wrong
- Gets spatial relation wrong
- Confuses foreground/background

## OCR failures

- Misreads text
- Skips small text
- Mixes nearby text fields
- Reads decorative text as data
- Fails handwritten text
- Fails rotated/low-contrast text

## Document and chart failures

- Misreads axis labels
- Misreads units
- Confuses rows/columns
- Infers a trend not present
- Fails to cite source location
- Produces numerically impossible answer

## Reasoning failures

- Answers a different question
- Uses language priors instead of image evidence
- Makes a plausible but unsupported inference
- Fails multi-step comparison
- Fails multi-image comparison

## Calibration failures

- Overconfident when image is ambiguous
- Does not say “cannot determine”
- Gives exact values from blurry evidence
- Hides uncertainty behind fluent wording

## Instruction-following failures

- Gives a caption instead of the requested format
- Ignores JSON/schema requirements
- Refuses a safe request
- Fails to follow multi-step instructions

## Safety and privacy failures

- Identifies a person when it should not
- Infers sensitive attributes from appearance
- Provides unsafe instructions from an image
- Reveals private data visible in a screenshot

## Agent/action failures

- Clicks wrong UI element
- Does not verify result
- Takes destructive action without confirmation
- Loops after failed action
- Misreads disabled vs active controls

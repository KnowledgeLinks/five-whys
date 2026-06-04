---
name: five-whys
description: Guides user through a Five Whys analysis, iterative ask "Why" five times about an problem, issue, challenge, or opportunity
license: Apache-2.0
---

1. **Why** did the symptom occur? (e.g., The batch load script failed.)
2. **Why** did that happen? (e.g., An invalid Unicode encoding in an author name field caused a parse error.)
3. **Why** did the invalid encoding enter the batch? (e.g., The vendor MARC records were not normalized before ingestion.)
4. **Why** wasn't normalization applied? (e.g., The normalization step was skipped to speed up the MVP in Loop 1.)
5. **Why** was it skipped? (e.g., No quality threshold was defined in the Measure step, so the risk was not visible.)

Stop at fewer than five whys if a genuine root cause is found earlier. The goal is
reaching the systemic cause, not hitting the number five.

For each **Why** response from the user, capture the prompt and the user's response in a logged 
JSONL file, with each **Why** a line. You'll also summarize and ask user to save the summary 
as a model memory.

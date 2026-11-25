# Speed Dating Analysis
> Descriptive statistical analysis of Columbia University speed dating experiments (2002-2004). Explores what drives mutual attraction across 10 research questions covering attributes, gender differences, demographics, and situational factors.

## Key Results

### Dataset highlights

8,378 rows (one per participant and date, so each date appears twice) across 21 waves. 551 participants (274 women, 277 men). Dataset spans 2002-2004.

### Research questions

The project investigates 10 research questions through descriptive statistics and visualizations (no ML):

1. What are the least desirable attributes in a male vs. female partner?
2. How important do people think attractiveness is vs. its real impact on decisions?
3. Are shared interests more important than shared racial background?
4. Can people accurately predict their own perceived value in the dating market?
5. Is it better to be the first or last date of the evening?
6. Does season affect attraction?
7. Do experimental variations (budget constraint, different M.C., magazine/book props) influence decisions?
8. Does field of study influence decisions or partner evaluation?
9. Does career influence matching success?
10. Do hobbies and activities influence matching success?

## Tech Stack

| Category | Technology |
|----------|------------|
| Language | Python 3.13 |
| Data | pandas, numpy |
| Visualization | matplotlib, seaborn |
| Statistics | scipy |
| Notebook | Jupyter |
| Package Manager | uv |

## Installation

```bash
uv sync
```

Requires [uv](https://docs.astral.sh/uv/).

## Usage

```bash
uv run jupyter notebook
```

- **Main analysis**: `speed_dating_analysis.ipynb` -- single consolidated notebook with all 10 questions.
- `plots/` -- the 18 figures saved by the notebook.

## Data

**Source**: Columbia University Speed Dating dataset (Fisman & Iyengar, 2002-2004) -- 8,378 rows across 21 waves. Provided as a Jedha training course project.

Participants had 4-minute dates with all opposite-gender attendees, rated partners on 6 attributes (Attractiveness, Sincerity, Intelligence, Fun, Ambition, Shared Interests), and indicated whether they wanted a second date.

- `data/input/Speed_Dating_Data.csv` -- raw data (versioned). The data key PDF is git-ignored.
- The notebook builds the cleaned dataset (6,872 rows) in memory and does not write it to disk.
- `data/MAPPINGS.json` -- value labels for coded columns (reference file; the notebook defines its own labels inline).

Licence: no licence stated by the source. The data is not covered by the code licence.

## License

Code: MIT, see `LICENSE`.


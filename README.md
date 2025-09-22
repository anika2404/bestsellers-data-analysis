# bestsellers-data-analysis

This project performs basic data analysis on a dataset of best-selling books using Python and pandas. It includes data cleaning, transformation, and exporting summary insights such as top authors and average ratings by genre.

---

## 📁 Dataset

The dataset used is `bestsellers.csv`, which includes information on top-selling books such as:

- Title
- Author
- Genre
- Price
- User Rating
- Publication Year

---

## ⚙️ Features

The script includes the following steps:

1. **Read the CSV file** into a pandas DataFrame.
2. **Preview and inspect** the dataset (head, shape, columns, describe).
3. **Remove duplicates** for data cleanliness.
4. **Rename columns** for clarity:
   - `Name` → `Title`
   - `Year` → `Publication Year`
   - `User Rating` → `Rating`
5. **Convert `Price` to float** for numerical analysis.
6. **Count number of books per author**.
7. **Compute average rating by genre**.
8. **Export results**:
   - Top 10 selling authors → `top_authors.csv`
   - Average rating by genre → `avg_rating_by_genre.csv`

---

## 📊 Outputs

- `top_authors.csv`: Top 10 most frequent authors in the dataset.
- `avg_rating_by_genre.csv`: Average user rating grouped by genre.

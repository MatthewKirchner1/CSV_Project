import csv
from datetime import datetime
import matplotlib.pyplot as plt


def main():
    def new_file(weather_report_csv):
        open_file = open(weather_report_csv, "r")

        csv_file = csv.reader(open_file, delimiter=",")

        header_row = next(csv_file)

        # The enumerate() fcn returns both the index of each item and the value of each
        # item as you loop trough a list

        enum = {}

        for index, column_header in enumerate(header_row):
            enum[column_header] = index

        print(enum)

        high_index = enum["TMAX"]
        low_index = enum["TMIN"]
        date_index = enum["DATE"]
        name_index = enum["NAME"]

        # Get high temps
        highs = []
        lows = []
        dates = []

        for row in csv_file:
            try:
                high = int(row[high_index])
                low = int(row[low_index])
                converted_date = datetime.strptime(row[date_index], "%Y-%m-%d")
                station = row[name_index]
            except ValueError:
                print(f"Missing data for {converted_date}")
            else:
                highs.append(int(row[high_index]))
                lows.append(int(row[low_index]))
                dates.append(converted_date)
                station = row[name_index]

        return (highs, lows, dates, station)

    def plot(high, low, date, title):

        fig = plt.figure()

        plt.plot(date, high, c="red")
        plt.plot(date, low, c="blue")

        plt.fill_between(date, high, low, facecolor="blue", alpha=0.1)

        plt.title(title, fontsize=16)
        plt.xlabel("Date", fontsize=16)
        plt.ylabel("Temperature (F)", fontsize=16)
        plt.tick_params(axis="both", which="major", labelsize=16)

        fig.autofmt_xdate()

        return plt.plot

    highs1, lows1, dates1, station1 = new_file("sitka_weather_2018_simple.csv")
    plot1 = plot(highs1, lows1, dates1, station1)
    print(station1)

    highs2, lows2, dates2, station2 = new_file("death_valley_2018_simple.csv")
    plot2 = plot(highs2, lows2, dates2, station2)
    print(station2)

    fig, ax = plt.subplots(2, 1, sharex=True)
    fig.suptitle("Temperature compairson between " + station1 + " and " + station2)
    ax[0].plot(dates1, highs1, c="red")
    ax[0].plot(dates1, lows1, c="blue")
    ax[0].fill_between(dates1, highs1, lows1, facecolor="blue", alpha=0.1)
    ax[0].set_title(station1)

    ax[1].plot(dates2, highs2, c="red")
    ax[1].plot(dates2, lows2, c="blue")
    ax[1].fill_between(dates2, highs2, lows2, facecolor="blue", alpha=0.1)
    ax[1].set_title(station2)
    ax[1].tick_params(axis="both", which="major", labelsize=16)
    fig.autofmt_xdate()

    plt.show()


main()
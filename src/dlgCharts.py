from bisect import bisect_left, bisect_right

from PySide6.QtCore import QDate, Qt
from PySide6.QtWidgets import *
from PySide6.QtCharts import QBarCategoryAxis, QBarSeries, QBarSet, QChart, QChartView, QValueAxis

from api import total, totalByDate, totalByEvent
from ui_dlgCharts import Ui_Dialog

class dlgCharts(QDialog):
    def __init__(self, data, parent=None):
        super().__init__(parent)
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.showMaximized()

        self.data = data
        minDate = QDate.fromString(data[0][0], 'yyyy/MM/dd')
        maxDate = QDate.fromString(data[-1][0], 'yyyy/MM/dd')
        self.ui.startDateEdit.setDateRange(minDate, maxDate)
        self.ui.endDateEdit.setDateRange(minDate, maxDate)
        self.ui.startDateEdit.setDate(minDate)
        self.ui.endDateEdit.setDate(maxDate)

        self.__update_totalChart(*total(data))
        self.__update_eventChart(totalByEvent(data))
        self.__update_dateChart(totalByDate(data))

        self.ui.startDateEdit.editingFinished.connect(self.__updateCharts)
        self.ui.endDateEdit.editingFinished.connect(self.__updateCharts)

    @staticmethod
    def createChart(chartView: QChartView, title, xAxis, yAxisList):
        chart = QChart()
        chart.setTitle(title)
        chart.setAnimationOptions(QChart.SeriesAnimations)

        series = QBarSeries()
        for axisName, data in yAxisList:
            barSet = QBarSet(axisName)
            barSet.append(data)
            series.append(barSet)
        chart.addSeries(series)

        axisX = QBarCategoryAxis()
        axisX.append(xAxis)
        chart.addAxis(axisX, Qt.AlignBottom)
        series.attachAxis(axisX)

        axisY = QValueAxis()
        axisY.setLabelFormat('%d')
        chart.addAxis(axisY, Qt.AlignLeft)
        series.attachAxis(axisY)

        chartView.setChart(chart)

    def __update_totalChart(self, total_in, total_out):
        self.createChart(
            chartView = self.ui.totalView,
            title     = '总收支',
            xAxis     = ['收入', '支出'], 
            yAxisList = [
                ('金额', [total_in, total_out])
            ]
        )

    def __update_eventChart(self, events):
        self.createChart(
            chartView = self.ui.eventView,
            title     = '收支分类',
            xAxis     = list(events.keys()),
            yAxisList = [
                ('收入', list(map(lambda x: x[0], events.values()))),
                ('支出', list(map(lambda x: x[1], events.values())))
            ]
        )

    def __update_dateChart(self, dates):
        self.createChart(
            chartView = self.ui.dateView,
            title     = '每日收支',
            xAxis     = list(dates.keys()),
            yAxisList = [
                ('收入', list(map(lambda x: x[0], dates.values()))),
                ('支出', list(map(lambda x: x[1], dates.values())))
            ]
        )

    def __updateCharts(self):
        startDate = self.ui.startDateEdit.text()
        endDate = self.ui.endDateEdit.text()
        left = bisect_left(self.data, startDate, key=lambda x: x[0])
        right = bisect_right(self.data, endDate, key=lambda x: x[0])
        data = self.data[left:right]
        self.__update_totalChart(*total(data))
        self.__update_eventChart(totalByEvent(data))
        self.__update_dateChart(totalByDate(data))

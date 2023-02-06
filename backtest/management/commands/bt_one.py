import plotly.io
import matplotlib
import matplotlib.pyplot as plt
from django.core.management.base import BaseCommand
from backtest import backtest_one
from backtrader_plotly.plotter import BacktraderPlotly
from backtrader_plotly.scheme import PlotScheme


class Command(BaseCommand):
    help = 'Installs packages not available in Pypi'

    def add_arguments(self, parser) -> None:
        parser.add_argument("strategy", type=str, help="Insert Strat")
        parser.add_argument("stock", type=str, help="Pick stock symbol")
        # return super().add_arguments(parser)

    def handle(self, *args, **options):
        strategy = options["strategy"].lower()
        stock = options["stock"].upper() + ".AX"
        result, cerebro, cash = backtest_one.main(strategy, stock)

        SIZE = 6
        COLOR = 'white'
        BACKGROUND = "#101622"
        GRID = "0.4"

        def default_colors(color=COLOR, size=SIZE, background=BACKGROUND, grid=GRID):
            matplotlib.use('Agg')
            plt.style.use('fivethirtyeight')
            plt.rcParams["figure.figsize"] = (10, 6)
            plt.rcParams['lines.linewidth'] = 2.5
            plt.rcParams['lines.color'] = "0.5"

            plt.rcParams["font.size"] = size
            plt.rcParams['axes.labelsize'] = size
            plt.rcParams['ytick.labelsize'] = size
            plt.rcParams['xtick.labelsize'] = size

            plt.rcParams['text.color'] = color
            plt.rcParams['axes.labelcolor'] = color
            plt.rcParams['xtick.color'] = color
            plt.rcParams['ytick.color'] = color

            plt.rcParams['axes.grid.axis'] = 'both'
            plt.rcParams['grid.linewidth'] = 0.1
            plt.rcParams['grid.color'] = grid
            # plt.rcParams['axes.edgecolor']="0.2"
            plt.rcParams['axes.linewidth'] = 0

        # plt.rcParams['grid.linewidth']=0

            plt.rcParams['figure.facecolor'] = background
            plt.rcParams['axes.facecolor'] = background
            plt.rcParams["savefig.dpi"] = 120
            dpi = plt.rcParams["savefig.dpi"]
            width = 700
            height = 1200
            plt.rcParams['figure.figsize'] = height/dpi, width/dpi
            plt.rcParams["savefig.facecolor"] = background
            plt.rcParams["savefig.edgecolor"] = background

            plt.rcParams['legend.fontsize'] = SIZE + 2
            plt.rcParams['legend.title_fontsize'] = SIZE + 2
            plt.rcParams['legend.labelspacing'] = 0.25
            plt.rcParams['image.cmap'] = 'tab10'

            plt.ioff()

        default_colors()
        cerebro.plot(
            linevalues=False,
            valuetags=False,
            loc='white',  # changes color for 'line on close' plot otherwise it will plot black on black
            grid=False  # the default gridlines didn't look good w/ dark background

        )

import matplotlib
import matplotlib.pyplot as plt
from django.core.management.base import BaseCommand
from backtest import backtest_one
from datetime import datetime


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
        filename = f"{stock}_{strategy}_{datetime.now()}"

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

        def saveplots(cerebro, numfigs=1, iplot=True, start=None, end=None,
                      width=16, height=9, dpi=300, tight=True, use=None, file_path='', **kwargs):

            from backtrader import plot
            if cerebro.p.oldsync:
                plotter = plot.Plot_OldSync(**kwargs)
            else:
                plotter = plot.Plot(**kwargs)

            figs = []
            for stratlist in cerebro.runstrats:
                for si, strat in enumerate(stratlist):
                    rfig = plotter.plot(strat, figid=si * 100,
                                        numfigs=numfigs, iplot=iplot,
                                        start=start, end=end, use=use)
                    figs.append(rfig)

            for fig in figs:
                for f in fig:
                    f.savefig(file_path, bbox_inches='tight')
            return figs

        default_colors()

        saveplots(cerebro, file_path=f'media/plots/{filename}.png',
                  linevalues=False,
                  valuetags=False,
                  loc='white',
                  grid=False,)

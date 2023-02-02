import plotly.io
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

        cerebro.plot()
        # scheme = PlotScheme(decimal_places=5, max_legend_text_width=16)
        # fig = cerebro.plot(BacktraderPlotly(show=False, scheme=scheme))

        # for i, each_run in enumerate(fig):
        #     for j, each_strategy_fig in enumerate(each_run):
        #         # open plot in browser
        #         each_strategy_fig.show()

        #         # save the html of the plot to a variable
        #         html = plotly.io.to_html(each_strategy_fig, full_html=False)

        #         # write html to disk
        #         plotly.io.write_html(
        #             each_strategy_fig, f'media/{i}_{j}.html', full_html=True)

import typer
from rich import print
from rich.panel import Panel
from rich.prompt import Prompt
import logging

from bot.client import BinanceFuturesClient
from bot.orders import create_order
from bot.validators import validate_side, validate_order_type, validate_price
from bot.logging_config import setup_logging

app = typer.Typer()


def interactive_menu():
    setup_logging()
    client = BinanceFuturesClient()

    while True:
        print(Panel.fit(
            "[bold cyan]Binance Futures Testnet Trading Bot[/bold cyan]\n\n"
            "1. Place MARKET Order\n"
            "2. Place LIMIT Order\n"
            "3. View Order History\n"
            "4. Exit"
        ))

        choice = Prompt.ask("Select option")

        try:
            if choice == "1":
                symbol = Prompt.ask("Symbol (e.g. BTCUSDT)")
                side = validate_side(Prompt.ask("Side (BUY/SELL)").upper())
                quantity = float(Prompt.ask("Quantity"))

                response = create_order(
                    client, symbol, side, "MARKET", quantity
                )

                print(f"[green]Order ID: {response['orderId']}[/green]")

            elif choice == "2":
                symbol = Prompt.ask("Symbol (e.g. BTCUSDT)")
                side = validate_side(Prompt.ask("Side (BUY/SELL)").upper())
                quantity = float(Prompt.ask("Quantity"))
                price = float(Prompt.ask("Price"))

                response = create_order(
                    client, symbol, side, "LIMIT", quantity, price
                )

                print(f"[green]Order ID: {response['orderId']}[/green]")

            elif choice == "3":
                symbol = Prompt.ask("Symbol")
                orders = client.client.futures_get_all_orders(symbol=symbol)

                for order in orders[-5:]:
                    print(Panel.fit(
                        f"""
Order ID: {order['orderId']}
Type: {order['type']}
Side: {order['side']}
Status: {order['status']}
Qty: {order['origQty']}
Price: {order['price']}
                        """
                    ))

            elif choice == "4":
                print("[bold red]Exiting...[/bold red]")
                break

            else:
                print("[red]Invalid option[/red]")

        except Exception as e:
            logging.error(str(e))
            print(f"[bold red]ERROR:[/bold red] {e}")


if __name__ == "__main__":
    interactive_menu()
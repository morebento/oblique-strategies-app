import streamlit as st
import obliquestrategies
import logging
from logging.handlers import TimedRotatingFileHandler

def setup_logger():
    """
    Set up the logger with a timed rotating file handler.
    Log rotation is set to occur weekly.
    """
    logger = logging.getLogger("ObliqueStrategiesApp")
    logger.setLevel(logging.INFO)

    handler = TimedRotatingFileHandler("app.log", when="W0", interval=1, backupCount=4)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)

    return logger

logger = setup_logger()

def get_random_strategy():
    """
    Get a random Oblique Strategy.

    Returns:
        str: A random Oblique Strategy from the oblique_strategies module.
    """
    try:
        strategy = obliquestrategies.get_strategy()
        logger.info("Successfully retrieved a random Oblique Strategy.")
        return strategy
    except Exception as e:
        logger.error(f"Error retrieving a random Oblique Strategy: {e}")
        return "Error retrieving strategy. Please try again."

def main():
    """
    Main function to run the Streamlit app.
    Displays a random Oblique Strategy on the page.
    """
    #st.title("Random Oblique Strategy")
    strategy = get_random_strategy()
    st.write(strategy)

if __name__ == "__main__":
    main()

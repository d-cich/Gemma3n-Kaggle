import asyncio
from dotenv import load_dotenv
load_dotenv("C:/Users/djcic/Downloads/Gemma3n Kaggle/Gemma3n-Kaggle/.env", override=True)
from browser_use import Agent
from browser_use.llm import ChatOllama
from browser_use.browser import BrowserSession

browser_session = BrowserSession()

agent = Agent(
    task="Order me a pizza from papa johns.  I'm located in Greenville, SC so look for stores near there."  
    + "I would like a large cheese pizza with no extra toppings.  If there's anything else that needs to be filled out that I haven't mentioned, "
    + "choose whatever option you want.  The delivery address is 300 Garlington Road.  Stop when you get to the section to enter payment.",
    llm=ChatOllama(model='gemma3n:e2b'),
    browser_session=browser_session,
    planner_llm=ChatOllama(model='gemma3n:e2b'),
)
    
    
async def main():
    await agent.run()
    await browser_session.close()


if __name__ == '__main__':
	asyncio.run(main())
"""
Basic Usage Example
Demonstrates simple browser automation with enhancements
"""

import asyncio
import random
from playwright.async_api import async_playwright
import sys
import os

# Add parent directory to path to import security module
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.GhostPilot import AdvancedBrowserAutomation


async def basic_automation_example():
    """
    Basic example of using the Advanced Browser Automation system
    """
    print("🚀 Starting Basic Automation Example...")
    
    # Initialize automation system
    automation = AdvancedBrowserAutomation()
    
    # Get realistic browser configuration
    user_agent = automation.get_realistic_user_agents()
    screen_config = automation.get_realistic_screen_configs()
    browser_args = automation.get_advanced_browser_args(user_agent, screen_config)
    headers = automation.get_advanced_headers()
    
    print(f"📱 User Agent: {user_agent[:50]}...")
    print(f"🖥️  Screen: {screen_config['width']}x{screen_config['height']}")
    
    async with async_playwright() as p:
        # Launch browser
        print("🌐 Launching browser...")
        browser = await p.chromium.launch(
            headless=False,  # Set to True for headless mode
            args=browser_args
        )
        
        # Create context
        context = await browser.new_context(
            viewport={
                'width': screen_config['width'],
                'height': screen_config['height']
            },
            device_scale_factor=screen_config['device_pixel_ratio'],
            extra_http_headers=headers
        )
        
        # Create page
        page = await context.new_page()
        
        # Apply browser enhancements
        print("🔧 Applying browser enhancements...")
        await automation.inject_browser_enhancements(page)
        await automation.add_human_behavior(page)
        
        # Navigate to example website
        print("🔗 Navigating to example.com...")
        await page.goto('https://example.com', wait_until='networkidle')
        
        # Simulate human reading time
        reading_time = random.uniform(2, 4)
        print(f"📖 Reading page for {reading_time:.1f} seconds...")
        await asyncio.sleep(reading_time)
        
        # Get page title
        title = await page.title()
        print(f"📄 Page Title: {title}")
        
        # Take screenshot
        print("📸 Taking screenshot...")
        await page.screenshot(path='example_screenshot.png')
        print("✅ Screenshot saved as 'example_screenshot.png'")
        
        # Scroll down
        print("⬇️  Scrolling down...")
        await page.evaluate('window.scrollBy(0, window.innerHeight / 2)')
        await asyncio.sleep(random.uniform(1, 2))
        
        # Get some text content
        content = await page.evaluate('document.body.innerText')
        print(f"📝 Page content preview: {content[:100]}...")
        
        # Clean up
        print("🧹 Cleaning up...")
        await browser.close()
        
    print("✨ Automation completed successfully!")


async def test_multiple_pages():
    """
    Example of navigating multiple pages
    """
    print("\n🚀 Testing Multiple Page Navigation...")
    
    automation = AdvancedBrowserAutomation()
    user_agent = automation.get_realistic_user_agents()
    screen_config = automation.get_realistic_screen_configs()
    browser_args = automation.get_advanced_browser_args(user_agent, screen_config)
    
    test_urls = [
        'https://example.com',
        'https://www.iana.org',
        'https://httpbin.org/user-agent'
    ]
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, args=browser_args)
        context = await browser.new_context(
            viewport={
                'width': screen_config['width'],
                'height': screen_config['height']
            }
        )
        page = await context.new_page()
        
        await automation.inject_browser_enhancements(page)
        await automation.add_human_behavior(page)
        
        for url in test_urls:
            print(f"\n🔗 Visiting: {url}")
            
            try:
                await page.goto(url, wait_until='networkidle', timeout=30000)
                
                # Simulate human behavior
                await asyncio.sleep(random.uniform(2, 4))
                
                title = await page.title()
                print(f"   📄 Title: {title}")
                
                # Random chance to scroll
                if random.random() > 0.5:
                    print("   ⬇️  Scrolling...")
                    await page.evaluate('window.scrollBy(0, 300)')
                    await asyncio.sleep(random.uniform(1, 2))
                
            except Exception as e:
                print(f"   ❌ Error: {e}")
            
            # Delay between pages
            await asyncio.sleep(random.uniform(2, 4))
        
        await browser.close()
    
    print("\n✨ Multiple page test completed!")


async def test_form_interaction():
    """
    Example of interacting with form elements
    """
    print("\n🚀 Testing Form Interaction...")
    
    automation = AdvancedBrowserAutomation()
    user_agent = automation.get_realistic_user_agents()
    screen_config = automation.get_realistic_screen_configs()
    browser_args = automation.get_advanced_browser_args(user_agent, screen_config)
    
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, args=browser_args)
        context = await browser.new_context(
            viewport={
                'width': screen_config['width'],
                'height': screen_config['height']
            }
        )
        page = await context.new_page()
        
        await automation.inject_browser_enhancements(page)
        await automation.add_human_behavior(page)
        
        # Navigate to a page with forms (example)
        print("🔗 Navigating to test page...")
        await page.goto('https://httpbin.org/forms/post')
        
        # Wait for page to load
        await asyncio.sleep(2)
        
        # Fill form with human-like delays
        print("✍️  Filling form...")
        
        # Type with random delays between characters
        await page.fill('input[name="custname"]', '')  # Clear first
        for char in "John Doe":
            await page.type('input[name="custname"]', char, delay=random.randint(50, 150))
        
        await asyncio.sleep(random.uniform(0.5, 1))
        
        # Fill other fields
        await page.fill('input[name="custtel"]', '1234567890')
        await asyncio.sleep(random.uniform(0.3, 0.8))
        
        await page.fill('input[name="custemail"]', 'test@example.com')
        await asyncio.sleep(random.uniform(0.5, 1))
        
        print("✅ Form filled successfully")
        
        # Note: We don't submit to avoid actually sending data
        print("ℹ️  (Not submitting form - this is just a demo)")
        
        await asyncio.sleep(2)
        await browser.close()
    
    print("✨ Form interaction test completed!")


async def main():
    """
    Main function to run examples
    """
    print("=" * 60)
    print("Advanced Browser Automation - Basic Examples")
    print("=" * 60)
    
    try:
        # Run basic example
        await basic_automation_example()
        
        # Ask user if they want to continue with more examples
        print("\n" + "=" * 60)
    print("All examples completed!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())60)
        response = input("Run multiple page navigation test? (y/n): ")
        if response.lower() == 'y':
            await test_multiple_pages()
        
        print("\n" + "=" * 60)
        response = input("Run form interaction test? (y/n): ")
        if response.lower() == 'y':
            await test_form_interaction()
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
    
    print("\n" + "=" * 60)

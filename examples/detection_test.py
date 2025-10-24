"""
Detection Testing Example
Tests the browser automation system against various detection services
"""

import asyncio
import sys
import os
from datetime import datetime

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from src.GhostPilot import AdvancedBrowserAutomation
from playwright.async_api import async_playwright


class DetectionTester:
    """Class to test browser automation against detection services"""
    
    def __init__(self):
        self.automation = AdvancedBrowserAutomation()
        self.test_sites = [
            {
                'name': 'Bot Sannysoft',
                'url': 'https://bot.sannysoft.com/',
                'wait_time': 8,
                'description': 'Comprehensive bot detection tests'
            },
            {
                'name': 'Are You Headless',
                'url': 'https://arh.antoinevastel.com/bots/areyouheadless',
                'wait_time': 5,
                'description': 'Headless browser detection'
            },
            {
                'name': 'PixelScan',
                'url': 'https://pixelscan.net/',
                'wait_time': 8,
                'description': 'Advanced fingerprinting analysis'
            },
            {
                'name': 'BrowserLeaks - WebRTC',
                'url': 'https://browserleaks.com/webrtc',
                'wait_time': 6,
                'description': 'WebRTC leak detection'
            },
            {
                'name': 'BrowserLeaks - Canvas',
                'url': 'https://browserleaks.com/canvas',
                'wait_time': 6,
                'description': 'Canvas fingerprinting test'
            }
        ]
    
    async def run_detection_tests(self, headless=False):
        """
        Run browser through various detection tests
        
        Args:
            headless: Whether to run in headless mode
        """
        print("=" * 70)
        print("🔍 BROWSER AUTOMATION DETECTION TESTING")
        print("=" * 70)
        print(f"⏰ Test started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"🖥️  Mode: {'Headless' if headless else 'Headed'}")
        print("=" * 70)
        
        # Get configuration
        user_agent = self.automation.get_realistic_user_agents()
        screen_config = self.automation.get_realistic_screen_configs()
        browser_args = self.automation.get_advanced_browser_args(user_agent, screen_config)
        
        print(f"\n📱 User Agent: {user_agent[:80]}...")
        print(f"🖥️  Screen: {screen_config['width']}x{screen_config['height']} @ {screen_config['device_pixel_ratio']}x")
        print(f"🎨 Color Depth: {screen_config['color_depth']}-bit")
        
        async with async_playwright() as p:
            print("\n🌐 Launching browser...")
            browser = await p.chromium.launch(
                headless=headless,
                args=browser_args
            )
            
            context = await browser.new_context(
                viewport={
                    'width': screen_config['width'],
                    'height': screen_config['height']
                },
                device_scale_factor=screen_config['device_pixel_ratio']
            )
            
            page = await context.new_page()
            
            # Apply enhancements
            print("🔧 Applying browser enhancements...")
            await self.automation.inject_browser_enhancements(page)
            await self.automation.add_human_behavior(page)
            print("✅ Enhancements applied successfully\n")
            
            # Run tests
            for i, test in enumerate(self.test_sites, 1):
                print("-" * 70)
                print(f"📋 Test {i}/{len(self.test_sites)}: {test['name']}")
                print(f"📄 Description: {test['description']}")
                print(f"🔗 URL: {test['url']}")
                
                try:
                    print(f"⏳ Navigating...")
                    await page.goto(test['url'], wait_until='networkidle', timeout=30000)
                    
                    print(f"⏱️  Waiting {test['wait_time']} seconds for analysis...")
                    await asyncio.sleep(test['wait_time'])
                    
                    # Try to capture some results
                    try:
                        page_title = await page.title()
                        print(f"📄 Page loaded: {page_title}")
                    except:
                        pass
                    
                    print(f"✅ Test completed")
                    
                    # Take screenshot
                    screenshot_name = f"detection_test_{i}_{test['name'].replace(' ', '_')}.png"
                    await page.screenshot(path=screenshot_name)
                    print(f"📸 Screenshot saved: {screenshot_name}")
                    
                except Exception as e:
                    print(f"❌ Error during test: {e}")
                
                # Delay between tests
                if i < len(self.test_sites):
                    print(f"⏸️  Waiting before next test...")
                    await asyncio.sleep(3)
            
            print("\n" + "=" * 70)
            print("🎯 DETECTION TESTING SUMMARY")
            print("=" * 70)
            print(f"✅ Completed {len(self.test_sites)} tests")
            print(f"📸 Screenshots saved in current directory")
            print(f"💡 Review screenshots to see detection results")
            print("\n📊 What to look for in results:")
            print("   ✓ 'webdriver' property should be: undefined or false")
            print("   ✓ Chrome/Navigator properties should appear normal")
            print("   ✓ No automation flags detected")
            print("   ✓ Canvas/WebGL fingerprints should be consistent")
            print("   ✓ No WebRTC IP leaks")
            print("=" * 70)
            
            if not headless:
                print("\n⏸️  Browser will stay open for manual inspection...")
                print("Press Ctrl+C to close")
                try:
                    await asyncio.sleep(3600)  # Keep open for inspection
                except KeyboardInterrupt:
                    print("\n👋 Closing browser...")
            
            await browser.close()
        
        print(f"\n⏰ Test completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


async def quick_webdriver_check():
    """
    Quick test to check if webdriver property is properly hidden
    """
    print("\n🔍 Quick WebDriver Detection Check")
    print("-" * 50)
    
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
        
        # Apply enhancements
        await automation.inject_browser_enhancements(page)
        
        # Check webdriver property
        webdriver_value = await page.evaluate('navigator.webdriver')
        chrome_exists = await page.evaluate('typeof window.chrome !== "undefined"')
        plugins_count = await page.evaluate('navigator.plugins.length')
        
        print(f"navigator.webdriver: {webdriver_value}")
        print(f"window.chrome exists: {chrome_exists}")
        print(f"navigator.plugins.length: {plugins_count}")
        
        if webdriver_value is None or webdriver_value is False:
            print("✅ WebDriver property properly hidden!")
        else:
            print("⚠️  WebDriver property detected!")
        
        if chrome_exists:
            print("✅ Chrome runtime present!")
        else:
            print("⚠️  Chrome runtime missing!")
        
        if plugins_count > 0:
            print(f"✅ Browser has {plugins_count} plugins!")
        else:
            print("⚠️  No plugins detected!")
        
        print("-" * 50)
        
        await asyncio.sleep(3)
        await browser.close()


async def main():
    """Main function"""
    print("\n" + "=" * 70)
    print("ADVANCED BROWSER AUTOMATION - DETECTION TESTING")
    print("=" * 70)
    
    print("\nSelect test mode:")
    print("1. Quick WebDriver check")
    print("2. Full detection test suite (headed mode)")
    print("3. Full detection test suite (headless mode)")
    print("4. Both headed and headless comparison")
    
    try:
        choice = input("\nEnter choice (1-4): ").strip()
        
        if choice == '1':
            await quick_webdriver_check()
        
        elif choice == '2':
            tester = DetectionTester()
            await tester.run_detection_tests(headless=False)
        
        elif choice == '3':
            tester = DetectionTester()
            await tester.run_detection_tests(headless=True)
        
        elif choice == '4':
            tester = DetectionTester()
            print("\n📍 Running HEADED mode tests first...")
            await tester.run_detection_tests(headless=False)
            
            print("\n" + "=" * 70)
            input("Press Enter to continue with HEADLESS mode tests...")
            
            print("\n📍 Running HEADLESS mode tests...")
            await tester.run_detection_tests(headless=True)
        
        else:
            print("❌ Invalid choice")
            return
        
        print("\n✨ All tests completed!")
        print("\n💡 Tips for interpreting results:")
        print("   - Green/Pass indicators = Good")
        print("   - Red/Fail indicators = Needs attention")
        print("   - Compare with regular browser for reference")
        print("   - Some tests may show false positives")
        
    except KeyboardInterrupt:
        print("\n\n⚠️  Interrupted by user")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    asyncio.run(main())
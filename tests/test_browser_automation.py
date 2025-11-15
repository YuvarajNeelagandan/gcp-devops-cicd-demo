"""Browser Automation Tests using Playwright

These tests demonstrate end-to-end browser automation,
perfect for QA/Test Automation portfolios.

Features:
- Multi-browser support (Chromium, Firefox, WebKit)
- Parallel test execution
- Screenshot capture on failure
- Video recording
- Network interception
- Mobile emulation
"""
import pytest
from playwright.sync_api import Page, expect
import os


# Mark tests as slow for selective execution
pytestmark = pytest.mark.slow


class TestWebAutomation:
    """End-to-end web automation test suite"""
    
    def test_google_search(self, page: Page):
        """Test Google search functionality"""
        # Navigate to Google
        page.goto("https://www.google.com")
        
        # Check title
        expect(page).to_have_title("Google")
        
        # Find search box and type
        search_box = page.get_by_role("combobox", name="Search")
        search_box.fill("DevOps CI/CD")
        
        # Submit search
        search_box.press("Enter")
        
        # Wait for results
        page.wait_for_selector("#search")
        
        # Verify search results loaded
        assert "DevOps" in page.content()
    
    def test_github_navigation(self, page: Page):
        """Test GitHub navigation and search"""
        # Visit GitHub
        page.goto("https://github.com")
        
        # Check homepage loaded
        expect(page).to_have_url("https://github.com/")
        
        # Find and click on search
        search_input = page.get_by_placeholder("Search GitHub")
        search_input.click()
        search_input.fill("pytest automation")
        
        # Press Enter to search
        search_input.press("Enter")
        
        # Wait for search results
        page.wait_for_selector("[data-testid='results-list']")
        
        # Verify results contain 'pytest'
        assert "pytest" in page.content().lower()
    
    def test_form_submission(self, page: Page):
        """Test form interaction on httpbin.org"""
        # Navigate to httpbin forms page
        page.goto("https://httpbin.org/forms/post")
        
        # Fill form fields
        page.fill("input[name='custname']", "Test User")
        page.fill("input[name='custtel']", "1234567890")
        page.fill("input[name='custemail']", "test@example.com")
        
        # Select delivery option
        page.select_option("select[name='size']", "medium")
        
        # Check terms checkbox
        page.check("input[name='topping'][value='bacon']")
        
        # Submit form
        page.click("button[type='submit']")
        
        # Verify submission
        page.wait_for_selector("pre")
        assert "Test User" in page.content()
    
    def test_screenshot_capability(self, page: Page):
        """Test screenshot capture capability"""
        page.goto("https://example.com")
        
        # Take full page screenshot
        screenshot_path = "test_screenshot.png"
        page.screenshot(path=screenshot_path, full_page=True)
        
        # Verify screenshot was created
        assert os.path.exists(screenshot_path)
        
        # Clean up
        if os.path.exists(screenshot_path):
            os.remove(screenshot_path)
    
    def test_network_interception(self, page: Page):
        """Test network request interception"""
        # Track network requests
        requests = []
        
        def handle_request(request):
            requests.append(request.url)
        
        page.on("request", handle_request)
        
        # Navigate to page
        page.goto("https://httpbin.org/get")
        
        # Verify requests were captured
        assert len(requests) > 0
        assert any("httpbin.org" in url for url in requests)


class TestMobileEmulation:
    """Mobile device emulation tests"""
    
    def test_mobile_viewport(self, page: Page):
        """Test mobile responsive design"""
        # Set mobile viewport
        page.set_viewport_size({"width": 375, "height": 667})
        
        # Navigate to responsive site
        page.goto("https://www.google.com")
        
        # Check mobile viewport
        viewport = page.viewport_size
        assert viewport["width"] == 375
        assert viewport["height"] == 667


class TestPerformance:
    """Performance testing scenarios"""
    
    def test_page_load_performance(self, page: Page):
        """Measure page load time"""
        import time
        
        start_time = time.time()
        page.goto("https://httpbin.org")
        load_time = time.time() - start_time
        
        # Assert page loads in reasonable time
        assert load_time < 5.0, f"Page took {load_time}s to load"
    
    def test_multiple_requests_performance(self, page: Page):
        """Test performance with multiple API requests"""
        import time
        
        endpoints = [
            "https://httpbin.org/status/200",
            "https://httpbin.org/get",
            "https://httpbin.org/headers",
        ]
        
        start_time = time.time()
        for endpoint in endpoints:
            page.goto(endpoint)
            page.wait_for_load_state("networkidle")
        
        total_time = time.time() - start_time
        
        # All requests should complete reasonably quickly
        assert total_time < 10.0, f"Total time: {total_time}s"


# Fixtures for Playwright
@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    """Configure browser context"""
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "record_video_dir": "test-videos/",
    }


@pytest.fixture(scope="function")
def page(page: Page):
    """Setup page for each test"""
    # Set default timeout
    page.set_default_timeout(30000)
    yield page
    # Cleanup happens automatically

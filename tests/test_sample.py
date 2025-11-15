"""Sample API Test Suite for CI/CD Demo"""
import requests
import pytest


def test_api_status_check():
    """Test that a public API endpoint is reachable"""
    response = requests.get('https://httpbin.org/status/200')
    assert response.status_code == 200, "API should return status 200"


def test_api_json_response():
    """Test JSON response from API"""
    response = requests.get('https://httpbin.org/json')
    assert response.status_code == 200
    data = response.json()
    assert 'slideshow' in data, "Response should contain 'slideshow' key"


def test_api_headers():
    """Test API headers"""
    response = requests.get('https://httpbin.org/headers')
    assert response.status_code == 200
    assert 'application/json' in response.headers.get('Content-Type', '').lower()


def test_simple_math():
    """Simple arithmetic test"""
    assert 2 + 2 == 4
    assert 10 - 5 == 5
    assert 3 * 3 == 9

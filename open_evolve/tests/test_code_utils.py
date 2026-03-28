"""
Tests for code utilities in openevolve.utils.code_utils
"""

import unittest
from openevolve.utils.code_utils import apply_diff, extract_diffs, extract_code_language


class TestCodeUtils(unittest.TestCase):
    """Tests for code utilities"""

    def test_extract_diffs(self):
        """Test extracting diffs from a response"""
        diff_text = """
        Let's improve this code:

        <<<<<<< SEARCH
        def hello():
            print("Hello")
        =======
        def hello():
            print("Hello, World!")
        >>>>>>> REPLACE

        Another change:

        <<<<<<< SEARCH
        x = 1
        =======
        x = 2
        >>>>>>> REPLACE
        """

        diffs = extract_diffs(diff_text)
        self.assertEqual(len(diffs), 2)
        self.assertEqual(
            diffs[0][0],
            """        def hello():
            print(\"Hello\")""",
        )
        self.assertEqual(
            diffs[0][1],
            """        def hello():
            print(\"Hello, World!\")""",
        )
        self.assertEqual(diffs[1][0], "        x = 1")
        self.assertEqual(diffs[1][1], "        x = 2")

    def test_apply_diff(self):
        """Test applying diffs to code"""
        original_code = """
        def hello():
            print("Hello")

        x = 1
        y = 2
        """

        diff_text = """
        <<<<<<< SEARCH
        def hello():
            print("Hello")
        =======
        def hello():
            print("Hello, World!")
        >>>>>>> REPLACE

        <<<<<<< SEARCH
        x = 1
        =======
        x = 2
        >>>>>>> REPLACE
        """

        expected_code = """
        def hello():
            print("Hello, World!")

        x = 2
        y = 2
        """

        result = apply_diff(original_code, diff_text)

        # Normalize whitespace for comparison
        self.assertEqual(
            result,
            expected_code,
        )

    def test_extract_code_language(self):
        """Test extracting language from code snippets"""
        # Python
        self.assertEqual(extract_code_language("import os"), "python")
        self.assertEqual(extract_code_language("from math import sin"), "python")
        self.assertEqual(extract_code_language("def my_func():"), "python")
        self.assertEqual(extract_code_language("class MyClass:"), "python")

        # Java
        self.assertEqual(extract_code_language("package com.example;"), "java")
        self.assertEqual(extract_code_language("public class Main {"), "java")

        # C++
        self.assertEqual(extract_code_language("#include <iostream>"), "cpp")
        self.assertEqual(extract_code_language("int main() {"), "cpp")
        self.assertEqual(extract_code_language("void main() {"), "cpp")

        # JavaScript
        self.assertEqual(extract_code_language("function test() {}"), "javascript")
        self.assertEqual(extract_code_language("var x = 1;"), "javascript")
        self.assertEqual(extract_code_language("let y = 2;"), "javascript")
        self.assertEqual(extract_code_language("const z = 3;"), "javascript")
        self.assertEqual(extract_code_language("console.log('hi');"), "javascript")

        # Rust
        self.assertEqual(extract_code_language("module my_mod;"), "rust")
        self.assertEqual(extract_code_language("fn main() {"), "rust")
        self.assertEqual(extract_code_language("impl MyStruct {"), "rust")

        # SQL
        self.assertEqual(extract_code_language("SELECT * FROM table;"), "sql")
        self.assertEqual(extract_code_language("CREATE TABLE test (id INT);"), "sql")
        self.assertEqual(extract_code_language("INSERT INTO table VALUES (1);"), "sql")

        # Unknown
        self.assertEqual(extract_code_language("Just some plain text"), "unknown")
        self.assertEqual(extract_code_language('print("Hello")'), "unknown")


if __name__ == "__main__":
    unittest.main()

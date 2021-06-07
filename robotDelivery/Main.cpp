//
// Created by Matthew Zaldana on 3/21/2021.
//
#include <iostream>
#include <iomanip>
#include <fstream>

using namespace std;


#ifndef INTERSECTION_H
#define INTERSECTION_H
class Intersection {
private:
    int[] intersection;
public:
    Intersection();
    int edges();
    allVertices();
};

int main() {
    // Instantiates instance of class ifstream to open file
    ifstream inputFile("input.txt");
    // Save first line as number of intersections
    string lines;
    istringstream iss(lines);
    int numOfIntersections = stoi(lines);
    // Create empty 2d array for values of intersections
    int matrixValues[numOfIntersections][numOfIntersections];
    // While not the end of the file, save values
    int line = 0;
    while (inputFile.eof()) {
        for (int i = 0; i < numOfIntersections; i++) {
            matrixValues[line][i] = inputFile.get();
        }
        line++;
    }
    cout << numOfIntersections;
    return 0;
}
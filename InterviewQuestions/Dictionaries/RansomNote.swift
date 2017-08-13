//
//  RansomNote.swift
//  InterviewPrep
//
//  Created by Amrutha Varshini on 7/30/17.
//  Copyright © 2017 mantrarush. All rights reserved.
//

import Foundation
// Hacker Rank: https://www.hackerrank.com/challenges/ctci-ransom-note
//A kidnapper wrote a ransom note but is worried it will be traced back to him. He found a magazine and wants to know if he can cut out whole words from it and use them to create an untraceable replica of his ransom note. The words in his note are case-sensitive and he must use whole words available in the magazine, meaning he cannot use substrings or concatenation to create the words he needs.
//
//Given the words in the magazine and the words in the ransom note, print Yes if he can replicate his ransom note exactly using whole words from the magazine; otherwise, print No.
//
//Input Format
//
//The first line contains two space-separated integers describing the respective values of  (the number of words in the magazine) and  (the number of words in the ransom note).
//The second line contains  space-separated strings denoting the words present in the magazine.
//The third line contains  space-separated strings denoting the words present in the ransom note.
//
//Constraints
//
//
//.
//Each word consists of English alphabetic letters (i.e.,  to  and  to ).
//The words in the note and magazine are case-sensitive.
//Output Format
//
//Print Yes if he can use the magazine to create an untraceable replica of his ransom note; otherwise, print No.

func canPerformRansomNote(using magazineText: String, to kidnapperText: String) -> Bool {
    guard kidnapperText.characters.count < magazineText.characters.count else { return false }
    var magazineWordsHash: [String: Int] = [String: Int]()
    let magazineWords: [String] = magazineText.characters.split{$0 == " "}.map(String.init)
    let kidnapperWords: [String] = kidnapperText.characters.split{$0 == " "}.map(String.init)
    
    for word in magazineWords {
        if let wordCount = magazineWordsHash[word] {
            magazineWordsHash[word] = wordCount + 1
        } else {
            magazineWordsHash[word] = 1
        }
    }
    
    for word in kidnapperWords {
        guard let wordCount = magazineWordsHash[word], wordCount > 0 else { return false }
        magazineWordsHash[word] = wordCount - 1
    }
    return true
}


func handleInput() {
//    let _ = readLine()
//    let magazineText = readLine()
//    let kidnapperText = readLine()
//    guard let magText = magazineText, let ransomText = kidnapperText else {
//        print("No")
//        return
//    }
//    if canPerformRansomNote(using: magText, to: ransomText) {
//        print("Yes")
//    } else {
//        print("No")
//    }
    print(canPerformRansomNote(using: "two times three is not four", to: "two times two is four"))
}

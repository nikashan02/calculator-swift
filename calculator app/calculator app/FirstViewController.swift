//
//  FirstViewController.swift
//  calculator app
//
//  Created by Student03 on 2019-04-24.
//  Copyright © 2019 Student03. All rights reserved.
//

import UIKit
import Foundation

class FirstViewController: UIViewController {
    
    var numOnScreen:Double = 0;
    var privateNumDisplay = "";
    
    @IBOutlet weak var numDisplay: UILabel!
    
    @IBOutlet weak var ansDisplay: UILabel!
    
    @IBAction func numbers(_ sender: UIButton) {
        
        privateNumDisplay = privateNumDisplay + String(Double(sender.tag)-1.0)
        numDisplay.text = privateNumDisplay
        
    }
    
    @IBAction func calcButtons(_ sender: UIButton) {
        
        if numDisplay.text != "" {
            if sender.tag == 15 {
                privateNumDisplay = privateNumDisplay + "/"
            }
            else if sender.tag == 16 {
                privateNumDisplay = privateNumDisplay + "*"
            }
            else if sender.tag == 17 {
                privateNumDisplay = privateNumDisplay + "-"
            }
            else if sender.tag == 18 {
                privateNumDisplay = privateNumDisplay + "+"
            }
            else if sender.tag == 14 {
                privateNumDisplay = String(privateNumDisplay.dropLast())
            }
            else if sender.tag == 11 {
                numDisplay.text = ""
                ansDisplay.text = ""
                privateNumDisplay = ""
            }
            numDisplay.text = privateNumDisplay
        }
        
        if sender.tag == 12 {
            privateNumDisplay = privateNumDisplay + "("
            numDisplay.text = privateNumDisplay
        }
        
        if sender.tag == 13 {
            privateNumDisplay = privateNumDisplay + ")"
            numDisplay.text = privateNumDisplay
        }
        
        if sender.tag == 19 {
            privateNumDisplay = privateNumDisplay + "."
            numDisplay.text = privateNumDisplay
        }
        
        
        if sender.tag == 20 {
            let calculate = NSExpression(format: privateNumDisplay)
            
            let answer = calculate.expressionValue(with: nil, context: nil) as? Double
            
            let formatter = NumberFormatter()
            formatter.minimumFractionDigits = 0
            formatter.maximumFractionDigits = 2
            
            let value = formatter.string(from: NSNumber(value: answer!))

            ansDisplay.text = value
        }
    }
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view.
    }

}

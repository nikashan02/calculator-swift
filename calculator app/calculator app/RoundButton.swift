//
//  RoundButton.swift
//  calculator app
//
//  Created by Student03 on 2019-05-15.
//  Copyright © 2019 Student03. All rights reserved.
//

import UIKit

@IBDesignable
class RoundButton: UIButton {
    
    @IBInspectable var cornerRadius: CGFloat = 0 {
        didSet {
            self.layer.cornerRadius = cornerRadius
        }
    }
    
    
}

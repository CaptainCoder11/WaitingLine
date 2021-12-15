import { Component, ViewChild } from '@angular/core';
import { NgxOtpInputComponent, NgxOtpInputConfig } from 'ngx-otp-input';
import { CookieService } from 'ngx-cookie-service';

@Component({
  selector: 'otp',
  templateUrl: '../templates/otp.component.html',
})
export class OtpComponent {
  constructor(private cookieService: CookieService){}
  @ViewChild('ngxotp') ngxOtp: NgxOtpInputComponent;

  showNgxOtpInput = false;

  otpInputConfig: NgxOtpInputConfig = {
    otpLength: 6,
    autofocus: true,
    classList: {
      inputBox: 'my-super-box-class',
      input: 'my-super-class',
      inputFilled: 'my-super-filled-class',
      inputDisabled: 'my-super-disable-class',
      inputSuccess: 'my-super-success-class',
      inputError: 'my-super-error-class',
    },
  };

  regex: string;
  ariaLabels: string;
  ngxOtpDisable = false;
  status = null;

  fillResult = '';

  reload(): void {
    if(this.showNgxOtpInput==true)
    {
      this.showNgxOtpInput = false;
    }
    else{
    this.showNgxOtpInput = true;
    }
  }

  setRegex(): void {
    // TODO: proper string-to-regexp transform
    this.otpInputConfig.pattern = new RegExp(this.regex);
  }

  setAriaLabels(): void {
    const arr = this.ariaLabels.split(',');
    if (arr.length === 1) {
      this.otpInputConfig.ariaLabels = arr[0];
    } else {
      this.otpInputConfig.ariaLabels = arr.map((entry) =>
        entry.replace(/\s/g, '')
      );
    }
  }

  clear(): void {
    this.ngxOtp.clear();
  }

  verify(){
    (async () => {
      const rawResponse = await fetch('http://localhost:3333/verify_otp/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify({
          "email": "ruchitpatel65@gmail.com",
          "phone": 13456987654,
          "otp": this.fillResult
        })
      })
      console.log(this.fillResult);


      const content = await rawResponse.json();


      if(content.user_id!==undefined)
      {
        alert('OTP Verified!')
        console.log(content.user_id);
        this.cookieService.set('userid',content.user_id)
      }
      else if(content == "OTP Expired!")
      {
        alert('Expired! Please Request a new OTP')
        this.reload()
      }
      else{
        alert('Incorrect OTP!')
        this.clear();
      }

      console.log(content);
    })();

  }

}

import { Component } from '@angular/core';
import { AnimationItem } from 'lottie-web';
import { AnimationOptions } from 'ngx-lottie';


@Component({
  selector: 'loginanim',
  template: `
    <ng-lottie class="absolute left-0" width="650px" height="500px" [options]="options"></ng-lottie>
  `,
})
export class LoginanimComponent {
  options: AnimationOptions = {
    path: '../../assets/login.json',
  };

  animationCreated(animationItem: AnimationItem): void {
    console.log(animationItem);
  }
}

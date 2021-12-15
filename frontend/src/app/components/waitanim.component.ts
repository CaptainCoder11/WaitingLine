import { Component, Input } from '@angular/core';
import { AnimationItem } from 'lottie-web';
import { AnimationOptions } from 'ngx-lottie';


@Component({
  selector: 'waitanim',
  template: `
    <ng-lottie class="absolute right-80 bottom-10" width="550px" height="300px" [options]="options"></ng-lottie>
  `,
})

export class WaitinganimComponent {
  @Input() path: string = "waiting.json"
  options: AnimationOptions = {
    path: `../../assets/${this.path}`,
  };


animationCreated(animationItem: AnimationItem): void {
    console.log(animationItem);
  }



}

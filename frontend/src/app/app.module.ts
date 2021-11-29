import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { LoginComponent } from './components/login.component';
import { LogoComponent } from './components/logo.component';
import { LottieModule } from 'ngx-lottie';
import player from 'lottie-web';
import { LoginanimComponent } from './components/loginanim.component';

export function playerFactory() {
  return player;
}

@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    LogoComponent,
    LoginanimComponent
  ],
  imports: [
    BrowserModule.withServerTransition({ appId: 'serverApp' }),
    LottieModule.forRoot({ player: playerFactory })
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }

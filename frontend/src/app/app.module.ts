import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppComponent } from './app.component';
import { LoginComponent } from './components/login.component';
import { LogoComponent } from './components/logo.component';
import { LottieModule } from 'ngx-lottie';
import player from 'lottie-web';
import { LoginanimComponent } from './components/loginanim.component';
import { OtpComponent } from './components/otp.component';
import { NgxOtpInputModule } from 'ngx-otp-input';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { StoresComponent } from './components/stores.component';
import { HttpClientModule } from '@angular/common/http';
import { CookieService } from 'ngx-cookie-service';
import { CustomerDashboardComponent } from './components/customerdashboard.component';
import { WaitinganimComponent } from './components/waitanim.component';

export function playerFactory() {
  return player;
}


@NgModule({
  declarations: [
    AppComponent,
    LoginComponent,
    LogoComponent,
    LoginanimComponent,
    OtpComponent,
    StoresComponent,
    CustomerDashboardComponent,
    WaitinganimComponent,
  ],
  imports: [
    BrowserModule.withServerTransition({ appId: 'serverApp' }),
    LottieModule.forRoot({ player: playerFactory }),
    NgxOtpInputModule,
    FormsModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [CookieService],
  bootstrap: [AppComponent]
})
export class AppModule { }

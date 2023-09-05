import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { HTTP_INTERCEPTORS, HttpClientModule } from '@angular/common/http';

import { AppComponent } from './app.component';
import { LoginPageComponent } from './login-page/login-page.component';
import { AuthLayoutComponent } from './shared/layouts/auth-layout/auth-layout.component';
import { SiteLayoutComponent } from './shared/layouts/site-layout/site-layout.component';
import { RegisterPageComponent } from './register-page/register-page.component';
import { TokenInterceptor } from './shared/classes/token.interceptor';
import { OverviewPageComponent } from './overview-page/overview-page.component';
import { AnalyticsPageComponent } from './analytics-page/analytics-page.component';
import { ArchivePageComponent } from './archive-payments-page/archive-payments-page.component';
import { CurrentPaymentsPageComponent } from './current-payments-page/current-payments-page.component';
import { LoaderComponent } from './shared/components/loader/loader.component';
import { CurrentPaymentsFormComponent } from './current-payments-page/current-payments-form/current-payments-form.component';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MaterialModule } from 'src/material.module';
import {ToastrModule} from 'ngx-toastr';
import { AddCurrentPaymentsDialogComponent } from './add-current-payments-dialog/add-current-payments-dialog.component'
import { DatePipe } from '@angular/common';
import { WordDialogComponent } from './word-dialog/word-dialog.component';
import { PdfViewerModule } from 'ng2-pdf-viewer';
import {NgxExtendedPdfViewerModule} from 'ngx-extended-pdf-viewer'
import { NgbModalModule } from '@ng-bootstrap/ng-bootstrap';
import { CommentmentsDialodComponent } from './commentments-dialod/commentments-dialod.component';


@NgModule({
  declarations: [
    AppComponent,
    LoginPageComponent,
    AuthLayoutComponent,
    SiteLayoutComponent,
    RegisterPageComponent,
    OverviewPageComponent,
    AnalyticsPageComponent,
    ArchivePageComponent,
    CurrentPaymentsPageComponent,
    LoaderComponent,
    CurrentPaymentsFormComponent,
    AddCurrentPaymentsDialogComponent,
    WordDialogComponent,
    CommentmentsDialodComponent,
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MaterialModule,
    ToastrModule.forRoot(),
    PdfViewerModule,
    NgxExtendedPdfViewerModule,
    NgbModalModule,

  ],
  providers: [DatePipe, 
  {
    provide:HTTP_INTERCEPTORS,
    multi:true,
    useClass:TokenInterceptor
  }],
  bootstrap: [AppComponent]
})
export class AppModule { }

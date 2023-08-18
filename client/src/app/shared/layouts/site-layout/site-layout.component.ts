import { AfterViewInit, Component, ElementRef, ViewChild } from '@angular/core';
import { AuthService } from '../../services/auth.services';
import { Router } from '@angular/router';
import { MaterialService } from '../../classes/material.service';

@Component({
  selector: 'app-site-layout',
  templateUrl: './site-layout.component.html',
  styleUrls: ['./site-layout.component.css']
})
export class SiteLayoutComponent implements AfterViewInit{

  @ViewChild('floating') floatingRef!:ElementRef

  constructor(private auth:AuthService, private router:Router){

  }

  ngAfterViewInit(): void {
    MaterialService.initializeFloatingButton(this.floatingRef)
  }

  links=[

    {url:'/overview', name:'Обзор'},
    {url:'/currentpayments', name:'Текущие платежи'},
    {url:'/archive', name:'Архив'},
    {url:'/analytics', name:'Аналитика'},

  ]

  logout(event:Event){
    event.preventDefault()
    this.auth.logout()
    this.router.navigate(['/login'])
  }


}

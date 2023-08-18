import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CurrentPaymentsPageComponent } from './current-payments-page.component';

describe('CurrentPaymentsPageComponent', () => {
  let component: CurrentPaymentsPageComponent;
  let fixture: ComponentFixture<CurrentPaymentsPageComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CurrentPaymentsPageComponent]
    });
    fixture = TestBed.createComponent(CurrentPaymentsPageComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

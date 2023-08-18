import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CurrentPaymentsFormComponent } from './current-payments-form.component';

describe('CurrentPaymentsFormComponent', () => {
  let component: CurrentPaymentsFormComponent;
  let fixture: ComponentFixture<CurrentPaymentsFormComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CurrentPaymentsFormComponent]
    });
    fixture = TestBed.createComponent(CurrentPaymentsFormComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});

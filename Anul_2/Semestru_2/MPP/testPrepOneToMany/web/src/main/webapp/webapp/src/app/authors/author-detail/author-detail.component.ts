
import {Location} from '@angular/common';
import {Component, Input, OnInit} from '@angular/core';
import {Author} from '../shared/author.model';
import {AuthorService} from '../shared/author.service';
import {ActivatedRoute, Params} from '@angular/router';
import {Observable} from 'rxjs';
import { switchMap } from 'rxjs/operators';

@Component({
  selector: 'app-author-detail',
  templateUrl: './author-detail.component.html',
  styleUrls: ['./author-detail.component.css']
})

export class AuthorDetailComponent implements OnInit {
  @Input() author: Author;

  constructor(private authorService: AuthorService,
              private route: ActivatedRoute,
              private location: Location) {

  }

  ngOnInit(): void {
    this.route.params.pipe(switchMap((params: Params) => this.authorService.getAuthor(+params['id'])))
      .subscribe(author => this.author = author);
  }

  goBack(): void {
    this.location.back();
  }
}
